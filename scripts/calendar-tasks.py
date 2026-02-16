#!/usr/bin/env python3
"""
Google Calendar tasks: accept invitation and add event
"""

import sys
from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# Check for credentials
token_file = Path.home() / ".openclaw/workspace/.credentials/google-calendar-token.json"
if not token_file.exists():
    print("❌ OAuth not configured yet!")
    print("Run: python3 scripts/setup-calendar-oauth.py")
    sys.exit(1)

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.events']
EST = ZoneInfo('America/New_York')

# Load credentials
creds = Credentials.from_authorized_user_file(str(token_file), SCOPES)
service = build('calendar', 'v3', credentials=creds)

print("✓ Connected to Google Calendar API\n")

# Task 1: List calendars (to find John's shared calendar)
print("=" * 60)
print("Available Calendars:")
print("=" * 60)
calendar_list = service.calendarList().list().execute()
for cal in calendar_list.get('items', []):
    print(f"  • {cal['summary']}")
    print(f"    ID: {cal['id']}")
    print(f"    Access: {cal.get('accessRole', 'unknown')}")
    print()

# Task 2: Add "go home" event today at 1:15 PM
print("=" * 60)
print("Creating Event: 'Go home' today at 1:15 PM EST")
print("=" * 60)

# Get today at 1:15 PM EST
now = datetime.now(EST)
event_time = now.replace(hour=13, minute=15, second=0, microsecond=0)

# If it's already past 1:15 PM, show a note
if now > event_time:
    print(f"⚠️  Note: 1:15 PM has already passed today ({now.strftime('%I:%M %p')})")
    print("Creating event anyway for records.\n")

event = {
    'summary': 'Go home',
    'start': {
        'dateTime': event_time.isoformat(),
        'timeZone': 'America/New_York',
    },
    'end': {
        'dateTime': (event_time + timedelta(minutes=15)).isoformat(),
        'timeZone': 'America/New_York',
    },
    'description': 'Added by Jack',
}

# Find John's calendar (look for his shared one)
johns_calendar_id = None
for cal in calendar_list.get('items', []):
    if 'John Alison' in cal['summary'] or cal.get('accessRole') == 'writer':
        johns_calendar_id = cal['id']
        break

if johns_calendar_id:
    print(f"Adding to calendar: {johns_calendar_id}")
    created_event = service.events().insert(calendarId=johns_calendar_id, body=event).execute()
    print(f"✓ Event created!")
    print(f"  Link: {created_event.get('htmlLink')}")
else:
    print("⚠️  Could not find John's shared calendar with write access")
    print("Available calendars listed above - which one should I use?")
