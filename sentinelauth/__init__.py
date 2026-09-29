"""
SentinelAuth Python SDK
Official Python client library for the SentinelAuth 2FA, OTP & TOTP API.
"""

from .client import SentinelAuth
from .exceptions import SentinelAuthError

__version__ = "1.0.0"
__all__ = ["SentinelAuth", "SentinelAuthError"]
