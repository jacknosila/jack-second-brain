#!/usr/bin/env python3
"""
Google Calendar OAuth2 Setup and Initial Auth Flow
Run this after getting credentials JSON from Google Cloud Console
"""

import os
import sys
from pathlib import Path

# Check if credentials file exists
creds_dir = Path.home() / ".openclaw/workspace/.credentials"
client_secret = creds_dir / "google-oauth-credentials.json"
token_file = creds_dir / "google-calendar-token.json"

if not client_secret.exists():
    print("❌ Missing google-oauth-credentials.json")
    print(f"\nExpected at: {client_secret}")
    print("\nFollow the setup guide in: scripts/setup-google-oauth.md")
    print("\nThen save the downloaded JSON as:")
    print(f"  {client_secret}")
    sys.exit(1)

print("✓ Found credentials file")
print("\nInstalling required packages...")

# Install Google API packages
os.system("pip3 install --quiet --upgrade google-auth-oauthlib google-auth-httplib2 google-api-python-client")

print("\n" + "="*60)
print("Starting OAuth2 Authorization Flow")
print("="*60)
print("\nThis will open a browser window.")
print("Log in as: jacknosila@gmail.com")
print("Grant permission to access your calendar.")
print("\n")

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/calendar.events']

creds = None

# Check if we already have valid credentials
if token_file.exists():
    creds = Credentials.from_authorized_user_file(str(token_file), SCOPES)

# If no valid credentials, run the auth flow
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        print("Refreshing expired token...")
        creds.refresh(Request())
    else:
        print("Starting new authorization flow...")
        flow = InstalledAppFlow.from_client_secrets_file(
            str(client_secret), SCOPES)
        creds = flow.run_local_server(port=0)
    
    # Save credentials for future use
    with open(token_file, 'w') as token:
        token.write(creds.to_json())
    print(f"\n✓ Credentials saved to: {token_file}")

print("\n🎉 SUCCESS! Google Calendar access configured!")
print("\nYou can now use the Calendar API to:")
print("  • Read your calendar")
print("  • Create events")
print("  • Modify events")
print("  • Accept calendar invitations")
