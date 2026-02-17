#!/usr/bin/env python3
"""
Send email via Gmail (primary) with AgentMail fallback.
Usage: python3 send-email.py <to_address> <subject> <body_file_or_text>
"""

import warnings
warnings.filterwarnings('ignore', category=UserWarning)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import os

def load_credentials():
    """Load credentials from jack.env file"""
    creds = {}
    creds_file = os.path.expanduser('~/.openclaw/workspace/.credentials/jack.env')
    
    with open(creds_file) as f:
        for line in f:
            line = line.strip()
            if '=' in line and not line.startswith('#'):
                key, value = line.split('=', 1)
                creds[key] = value.strip('"')
    
    return creds

def send_via_gmail(to_address, subject, body, creds):
    """Send email via Gmail SMTP"""
    gmail_user = creds.get('GMAIL_EMAIL')
    gmail_password = creds.get('GMAIL_APP_PASSWORD')
    
    if not gmail_user or not gmail_password:
        raise Exception("Gmail credentials not found")
    
    # Create message
    msg = MIMEMultipart()
    msg['From'] = f"Jack Nosila <{gmail_user}>"
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    # Send via Gmail SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.quit()
    
    return f"✅ Sent via Gmail ({gmail_user})"

def send_via_agentmail(to_address, subject, body, creds):
    """Send email via AgentMail API (fallback)"""
    # Add agentmail to path if needed
    sys.path.insert(0, '/Users/jacknosila/.openclaw/workspace/.venv/lib/python3.14/site-packages')
    
    from agentmail import AgentMail
    
    api_key = creds.get('AGENTMAIL_API_KEY')
    inbox_id = creds.get('AGENTMAIL_INBOX_ID')
    
    if not api_key or not inbox_id:
        raise Exception("AgentMail credentials not found")
    
    client = AgentMail(api_key=api_key)
    
    message = client.inboxes.messages.send(
        inbox_id=inbox_id,
        to=[to_address],
        subject=subject,
        text=body
    )
    
    return f"✅ Sent via AgentMail (fallback) - Message ID: {message.message_id}"

def main():
    if len(sys.argv) < 4:
        print("Usage: send-email.py <to_address> <subject> <body_file_or_text>")
        sys.exit(1)
    
    to_address = sys.argv[1]
    subject = sys.argv[2]
    body_input = sys.argv[3]
    
    # Check if body_input is a file
    if os.path.isfile(body_input):
        with open(body_input, 'r') as f:
            body = f.read()
    else:
        body = body_input
    
    # Load credentials
    creds = load_credentials()
    
    # Try Gmail first, fall back to AgentMail
    try:
        result = send_via_gmail(to_address, subject, body, creds)
        print(result)
    except Exception as e_gmail:
        print(f"⚠️  Gmail failed: {e_gmail}")
        print("⚠️  Falling back to AgentMail...")
        
        try:
            result = send_via_agentmail(to_address, subject, body, creds)
            print(result)
        except Exception as e_agent:
            print(f"❌ AgentMail also failed: {e_agent}")
            sys.exit(1)

if __name__ == "__main__":
    main()
