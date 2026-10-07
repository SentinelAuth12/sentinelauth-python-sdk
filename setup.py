from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sentinelauth",
    version="1.0.0",
    author="SentinelAuth",
    author_email="support@sentinelauth.com.au",
    description="Official Python SDK for SentinelAuth — SMS, Email OTP & 2FA / TOTP Authentication API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SentinelAuth12/sentinelauth-python-sdk",
    project_urls={
        "Documentation": "https://sentinelauth.com.au/docs/",
        "Website": "https://sentinelauth.com.au",
        "Bug Tracker": "https://github.com/SentinelAuth12/sentinelauth-python-sdk/issues",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[],
)
