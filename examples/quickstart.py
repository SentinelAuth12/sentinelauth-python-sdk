"""
SentinelAuth Python SDK Quickstart Example

Run: python examples/quickstart.py
"""

import os
from sentinelauth import SentinelAuth, SentinelAuthError

api_key = os.environ.get("SENTINELAUTH_API_KEY", "sk_test_demo_key")
client = SentinelAuth(api_key)

def main():
    try:
        print("--- 1. Send SMS OTP ---")
        sms_res = client.send_sms("+61412345678", app_name="MyPythonApp")
        print("SMS Dispatch Result:", sms_res)

        # print("\n--- 2. Verify OTP ---")
        # verify_res = client.verify_otp(sms_res.get("verification_id"), "123456")
        # print("Verification Result:", verify_res)

        print("\n--- 3. Enroll TOTP Factor ---")
        factor = client.enroll_totp(user_identifier="usr_py_5001", account_name="user@example.com", issuer="SentinelAuth")
        print("Enrolled Factor ID:", factor.get("factor_id"))
        print("QR Code URL:", factor.get("qr_code_url"))

        print("\n--- 4. Check Quota ---")
        quota = client.get_quota()
        print("Current Quota:", quota)

    except SentinelAuthError as e:
        print(f"SentinelAuth Error [{e.status_code}]: {e.message}")

if __name__ == "__main__":
    main()
