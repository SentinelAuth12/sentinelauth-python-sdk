"""
SentinelAuth Client Implementation
"""

import json
import urllib.request
import urllib.error
from typing import Optional, Dict, Any

from .exceptions import SentinelAuthError

class SentinelAuth:
    """Official SentinelAuth Python Client for 2FA, OTP & TOTP."""

    def __init__(self, api_key: str, base_url: str = "https://sentinelauth.com.au/wp-json/sentinelauth/v1", timeout: int = 15):
        if not api_key or not isinstance(api_key, str):
            raise SentinelAuthError("A valid SentinelAuth API key is required.")
        self.api_key = api_key.strip()
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _request(self, method: str, path: str, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Internal HTTP request handler using standard library urllib."""
        endpoint = f"{self.base_url}/{path.lstrip('/')}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "SentinelAuth-PythonSDK/1.0.0"
        }

        data_bytes = json.dumps(payload).encode("utf-8") if payload is not None else None
        req = urllib.request.Request(endpoint, data=data_bytes, headers=headers, method=method.upper())

        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                body = response.read().decode("utf-8")
                return json.loads(body) if body else {}
        except urllib.error.HTTPError as exc:
            try:
                err_data = json.loads(exc.read().decode("utf-8"))
                err_msg = err_data.get("message") or err_data.get("error") or str(exc)
            except Exception:
                err_data = {}
                err_msg = str(exc)
            raise SentinelAuthError(err_msg, status_code=exc.code, data=err_data)
        except urllib.error.URLError as exc:
            raise SentinelAuthError(f"Network error: {exc.reason}", status_code=500)

    def send_otp(self, to: str, channel: str = "sms", app_name: Optional[str] = None) -> Dict[str, Any]:
        """Dispatch a one-time verification code via SMS or Email."""
        if not to:
            raise SentinelAuthError("Recipient 'to' destination is required.")
        payload = {
            "to": to,
            "channel": channel.lower()
        }
        if app_name:
            payload["app_name"] = app_name
        return self._request("POST", "/send-otp", payload)

    def send_sms(self, to: str, app_name: Optional[str] = None) -> Dict[str, Any]:
        """Shorthand to dispatch SMS OTP."""
        return self.send_otp(to, channel="sms", app_name=app_name)

    def send_email(self, to: str, app_name: Optional[str] = None) -> Dict[str, Any]:
        """Shorthand to dispatch Email OTP."""
        return self.send_otp(to, channel="email", app_name=app_name)

    def verify_otp(self, verification_id: str, code: str) -> Dict[str, Any]:
        """Verify a user-submitted OTP code."""
        if not verification_id:
            raise SentinelAuthError("verification_id is required.")
        if not code:
            raise SentinelAuthError("Verification code is required.")
        return self._request("POST", "/verify-otp", {
            "verification_id": str(verification_id).strip(),
            "code": str(code).strip()
        })

    def enroll_totp(self, user_identifier: str, account_name: Optional[str] = None, issuer: Optional[str] = None) -> Dict[str, Any]:
        """Enroll a new TOTP 2FA Factor (Authenticator App)."""
        if not user_identifier:
            raise SentinelAuthError("user_identifier is required to enroll TOTP factor.")
        payload = {"user_identifier": user_identifier}
        if account_name:
            payload["account_name"] = account_name
        if issuer:
            payload["issuer"] = issuer
        return self._request("POST", "/totp/enroll", payload)

    def verify_totp(self, factor_id: str, code: str) -> Dict[str, Any]:
        """Verify a rolling 6-digit TOTP code from an authenticator app."""
        if not factor_id:
            raise SentinelAuthError("factor_id is required.")
        if not code:
            raise SentinelAuthError("6-digit code is required.")
        return self._request("POST", "/totp/verify", {
            "factor_id": str(factor_id).strip(),
            "code": str(code).strip()
        })

    def get_quota(self) -> Dict[str, Any]:
        """Retrieve monthly API quota usage and limits."""
        return self._request("GET", "/quota")
