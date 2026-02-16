#!/usr/bin/env python3
"""
Check Gmail inbox for unread messages
Requires: App-specific password or OAuth2 setup
"""

import imaplib
import email
from email.header import decode_header
import os
from pathlib import Path

# Load credentials
creds_file = Path.home() / ".openclaw/workspace/.credentials/jack.env"
creds = {}
with open(creds_file) as f:
    for line in f:
        if line.strip() and not line.startswith('#'):
            if '=' in line:
                key, val = line.strip().split('=', 1)
                creds[key] = val

GMAIL_USER = creds.get('GMAIL_EMAIL', '')
GMAIL_PASS = creds.get('GMAIL_APP_PASSWORD', creds.get('GMAIL_PASSWORD', ''))

def check_gmail():
    """Check Gmail for unread messages"""
    try:
        # Connect to Gmail IMAP
        print(f"Connecting to Gmail as {GMAIL_USER}...")
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(GMAIL_USER, GMAIL_PASS)
        
        # Select inbox
        mail.select('inbox')
        
        # Search for unread messages
        status, messages = mail.search(None, 'UNSEEN')
        message_ids = messages[0].split()
        
        print(f"\n📬 Found {len(message_ids)} unread messages\n")
        
        # Fetch recent unread (up to 5)
        for msg_id in message_ids[-5:]:
            status, msg_data = mail.fetch(msg_id, '(RFC822)')
            
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    
                    # Decode subject
                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        subject = subject.decode()
                    
                    # Get sender
                    from_addr = msg.get("From")
                    date = msg.get("Date")
                    
                    print(f"From: {from_addr}")
                    print(f"Subject: {subject}")
                    print(f"Date: {date}")
                    print("-" * 50)
        
        mail.close()
        mail.logout()
        
    except imaplib.IMAP4.error as e:
        print(f"❌ IMAP Error: {e}")
        print("\n⚠️  Gmail likely requires an App-Specific Password")
        print("Regular password won't work with IMAP anymore.")
        print("\nTo fix:")
        print("1. Go to Google Account Settings")
        print("2. Security → 2-Step Verification")
        print("3. App passwords → Generate new")
        print("4. Use that password in .credentials/jack.env")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    check_gmail()
