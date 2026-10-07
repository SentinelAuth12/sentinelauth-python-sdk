"""
SentinelAuth Exception Classes
"""

class SentinelAuthError(Exception):
    """Base exception for SentinelAuth SDK errors."""
    def __init__(self, message: str, status_code: int = 500, data: dict = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.data = data or {}

    def __str__(self):
        return f"[Status {self.status_code}] {self.message}"
