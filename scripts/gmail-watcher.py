#!/usr/bin/env python3
"""
gmail-watcher.py — checks jacknosila@gmail.com for new messages
and notifies the Claude Code session via Telegram.

Runs as a LaunchAgent every 5 minutes.
If a new message is from John (johnda102@gmail.com or johnalison@cmu.edu),
it sends the full content so Jack can act on it.
"""

import os
import json
import requests
from pathlib import Path
from datetime import datetime

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Config
GMAIL_TOKEN = Path.home() / '.config/jack/credentials/gmail_token.json'
STATE_FILE = Path.home() / '.config/jack/gmail-watcher-state.json'
BOT_TOKEN = '8066591103:AAEKDRMBmSM_byIXQj8aZyo4Tm8_UZgTIM0'
CHAT_ID = '7748852239'
JOHN_ADDRESSES = {'johnda102@gmail.com', 'johnalison@cmu.edu'}

SCOPES = [
    'https://mail.google.com/',
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/cloud-platform',
]


def send_telegram(text):
    requests.post(
        f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage',
        json={'chat_id': CHAT_ID, 'text': text}
    )


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {'last_history_id': None}


def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state))


def get_email_body(payload):
    """Extract plain text body from message payload."""
    if payload.get('mimeType') == 'text/plain':
        import base64
        data = payload.get('body', {}).get('data', '')
        if data:
            return base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')
    for part in payload.get('parts', []):
        body = get_email_body(part)
        if body:
            return body
    return ''


def main():
    # Load Gmail credentials
    creds = Credentials.from_authorized_user_file(str(GMAIL_TOKEN), SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        # Save refreshed token
        GMAIL_TOKEN.write_text(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    state = load_state()

    # Get current profile to check history ID
    profile = service.users().getProfile(userId='me').execute()
    current_history_id = int(profile['historyId'])

    if state['last_history_id'] is None:
        # First run — just record current state, don't spam
        save_state({'last_history_id': current_history_id})
        print(f"First run — recording history ID {current_history_id}")
        return

    last_history_id = int(state['last_history_id'])

    if current_history_id <= last_history_id:
        print("No new messages.")
        return

    # Fetch history since last check
    try:
        history = service.users().history().list(
            userId='me',
            startHistoryId=last_history_id,
            historyTypes=['messageAdded'],
            labelId='INBOX'
        ).execute()
    except Exception as e:
        print(f"History fetch error: {e}")
        save_state({'last_history_id': current_history_id})
        return

    new_messages = []
    for record in history.get('history', []):
        for msg_added in record.get('messagesAdded', []):
            new_messages.append(msg_added['message']['id'])

    if not new_messages:
        save_state({'last_history_id': current_history_id})
        return

    # Process each new message
    for msg_id in new_messages:
        msg = service.users().messages().get(
            userId='me', id=msg_id, format='full'
        ).execute()

        headers = {h['name']: h['value'] for h in msg['payload']['headers']}
        subject = headers.get('Subject', '(no subject)')
        from_addr = headers.get('From', '')
        date = headers.get('Date', '')

        # Check if from John
        is_from_john = any(addr in from_addr for addr in JOHN_ADDRESSES)

        if is_from_john:
            body = get_email_body(msg['payload'])
            body_preview = body[:500].strip() if body else '(no body)'
            text = (
                f"📧 New email from John:\n"
                f"From: {from_addr}\n"
                f"Subject: {subject}\n"
                f"Date: {date}\n\n"
                f"{body_preview}"
            )
        else:
            text = (
                f"📧 New email to jacknosila@gmail.com:\n"
                f"From: {from_addr}\n"
                f"Subject: {subject}"
            )

        send_telegram(text)
        print(f"Notified: {subject} from {from_addr}")

    save_state({'last_history_id': current_history_id})


if __name__ == '__main__':
    main()
