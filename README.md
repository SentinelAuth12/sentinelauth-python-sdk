# SentinelAuth Python SDK

Official Python library for **[SentinelAuth](https://sentinelauth.com.au)** — Developer-first Two-Factor Authentication (2FA), Multi-Factor Authentication (MFA), SMS OTP, Email Verification, and TOTP Authenticator APIs designed for Australia and global applications.

[![PyPI version](https://img.shields.io/pypi/v/sentinelauth.svg)](https://pypi.org/project/sentinelauth/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-%3E%3D3.7-blue.svg)](https://www.python.org/)
[![Website](https://img.shields.io/badge/website-sentinelauth.com.au-blue)](https://sentinelauth.com.au)
[![Documentation](https://img.shields.io/badge/docs-sentinelauth.com.au%2Fdocs-purple)](https://sentinelauth.com.au/docs/)

---

## Features

- ⚡ **Zero Dependencies** — Built on Python standard library (`urllib`), no heavy third-party packages required.
- 📱 **SMS OTP Verification** — Low-latency SMS delivery with automatic Australian number formatting (`+614...` or `04...`).
- 📧 **Email OTP Verification** — High-deliverability transactional verification emails.
- 🔐 **TOTP / 2FA Authenticator Support** — Enroll and verify Google Authenticator, Microsoft Authenticator, and Authy factors with QR code generation.
- 🛡️ **Zero-Plaintext Security** — Cryptographically hashed tokens; raw verification codes are never stored in databases.
- 🐍 **Modern Python 3.7+** — Full type hints and clear exception handling.

---

## Installation

Install using pip:

```bash
pip install sentinelauth
```

Or via Poetry / Pipenv:

```bash
poetry add sentinelauth
# or
pipenv install sentinelauth
```

---

## Quick Start

### 1. Initialize Client

Get your API key from the **[SentinelAuth Developer Dashboard](https://sentinelauth.com.au/dashboard/api-keys/)**.

```python
from sentinelauth import SentinelAuth

client = SentinelAuth("sk_live_your_api_key_here")
```

---

### 2. Send an OTP (SMS or Email)

#### Send SMS OTP:
```python
result = client.send_sms("+61412345678", app_name="MyCompany")

print("Verification ID:", result["verification_id"])
print("Status:", result["status"]) # 'pending' or 'sent'
```

#### Send Email OTP:
```python
result = client.send_email("alex@company.com", app_name="MyCompany")
print("Delivered to:", result["destination"])
```

---

### 3. Verify an OTP Code

When the user enters the 6-digit code received on their phone or email:

```python
from sentinelauth import SentinelAuth, SentinelAuthError

try:
    result = client.verify_otp(verification_id, code="123456")
    if result.get("verified"):
        print("✅ User successfully verified!")
except SentinelAuthError as e:
    print(f"❌ Verification failed [{e.status_code}]: {e.message}")
```

---

### 4. TOTP Authenticator (Google / Microsoft Authenticator)

#### Step A: Enroll a Factor & Show QR Code
```python
factor = client.enroll_totp(
    user_identifier="usr_100234",
    account_name="alex@example.com",
    issuer="MyCompany 2FA"
)

print("Factor ID:", factor["factor_id"])
print("QR Code URL for User:", factor["qr_code_url"])
print("Manual Secret Key:", factor["secret"])
```

#### Step B: Verify TOTP Rolling Code
```python
verification = client.verify_totp(
    factor_id=factor["factor_id"], # or 'usr_100234'
    code="849201" # 6 digits from authenticator app
)

if verification.get("verified"):
    print("✅ TOTP 2FA code is valid!")
```

---

### 5. Check API Quota & Usage

```python
quota = client.get_quota()
print(f"Plan: {quota['plan']}")
print(f"Used: {quota['used']} / {quota['monthly_limit']} requests")
print(f"Remaining: {quota['remaining']}")
```

---

## Links & Resources

- **Website:** [https://sentinelauth.com.au](https://sentinelauth.com.au)
- **API Documentation:** [https://sentinelauth.com.au/docs/](https://sentinelauth.com.au/docs/)
- **Dashboard & API Keys:** [https://sentinelauth.com.au/dashboard/api-keys/](https://sentinelauth.com.au/dashboard/api-keys/)
- **Interactive Sandbox & Testing:** [https://sentinelauth.com.au/dashboard/test-api/](https://sentinelauth.com.au/dashboard/test-api/)
- **GitHub Organization:** [https://github.com/SentinelAuth12](https://github.com/SentinelAuth12)

---

## License

MIT License © 2026 SentinelAuth.
