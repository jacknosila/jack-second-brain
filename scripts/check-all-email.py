#!/usr/bin/env python3
"""
Check both AgentMail and Gmail for unread messages
"""

import requests
import imaplib
import email
from email.header import decode_header
from pathlib import Path

def load_credentials():
    """Load credentials from jack.env"""
    creds_file = Path.home() / ".openclaw/workspace/.credentials/jack.env"
    creds = {}
    with open(creds_file) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                if '=' in line:
                    key, val = line.strip().split('=', 1)
                    creds[key] = val
    return creds

def check_agentmail(api_key):
    """Check AgentMail for unread messages"""
    try:
        url = "https://api.agentmail.to/v0/inboxes/jacknosila@agentmail.to/messages"
        headers = {"Authorization": f"Bearer {api_key}"}
        params = {"labels": "unread", "limit": 5}
        
        response = requests.get(url, headers=headers, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            count = data.get('count', 0)
            messages = data.get('messages', [])
            
            return {
                'success': True,
                'count': count,
                'messages': messages[:3]  # Top 3
            }
    except Exception as e:
        return {'success': False, 'error': str(e)}
    
    return {'success': False, 'error': 'Unknown error'}

def check_gmail(email_addr, app_password):
    """Check Gmail for unread messages"""
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(email_addr, app_password)
        mail.select('inbox')
        
        status, messages = mail.search(None, 'UNSEEN')
        message_ids = messages[0].split()
        
        unread_messages = []
        
        # Fetch up to 3 most recent unread
        for msg_id in message_ids[-3:]:
            status, msg_data = mail.fetch(msg_id, '(RFC822)')
            
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    
                    # Decode subject
                    subject = msg.get("Subject", "")
                    if subject:
                        decoded = decode_header(subject)[0]
                        if isinstance(decoded[0], bytes):
                            subject = decoded[0].decode(decoded[1] or 'utf-8')
                        else:
                            subject = decoded[0]
                    
                    from_addr = msg.get("From", "")
                    date = msg.get("Date", "")
                    
                    unread_messages.append({
                        'from': from_addr,
                        'subject': subject,
                        'date': date
                    })
        
        mail.close()
        mail.logout()
        
        return {
            'success': True,
            'count': len(message_ids),
            'messages': unread_messages
        }
        
    except Exception as e:
        return {'success': False, 'error': str(e)}

def main():
    """Check both email accounts"""
    creds = load_credentials()
    
    print("📧 Checking Email Accounts")
    print("=" * 50)
    
    # Check AgentMail
    print("\n📬 AgentMail (jacknosila@agentmail.to)")
    agentmail_result = check_agentmail(creds.get('AGENTMAIL_API_KEY', ''))
    
    if agentmail_result['success']:
        print(f"   Unread: {agentmail_result['count']}")
        if agentmail_result['messages']:
            for msg in agentmail_result['messages']:
                from_addr = msg.get('from', 'Unknown')
                subject = msg.get('subject', 'No subject')
                print(f"   • {from_addr}: {subject}")
    else:
        print(f"   ❌ Error: {agentmail_result.get('error')}")
    
    # Check Gmail
    print("\n📬 Gmail (jacknosila@gmail.com)")
    gmail_result = check_gmail(
        creds.get('GMAIL_EMAIL', ''),
        creds.get('GMAIL_APP_PASSWORD', '')
    )
    
    if gmail_result['success']:
        print(f"   Unread: {gmail_result['count']}")
        if gmail_result['messages']:
            for msg in gmail_result['messages']:
                from_addr = msg.get('from', 'Unknown')
                subject = msg.get('subject', 'No subject')
                print(f"   • {from_addr}: {subject}")
    else:
        print(f"   ❌ Error: {gmail_result.get('error')}")
    
    print("\n" + "=" * 50)
    
    # Return summary
    total_unread = 0
    if agentmail_result['success']:
        total_unread += agentmail_result['count']
    if gmail_result['success']:
        total_unread += gmail_result['count']
    
    print(f"Total unread across all accounts: {total_unread}")

if __name__ == "__main__":
    main()
