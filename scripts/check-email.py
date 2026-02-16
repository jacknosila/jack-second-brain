#!/usr/bin/env python3
"""Check AgentMail inbox for new unread messages."""

import sys
import os
import json

# Add the venv to the path
sys.path.insert(0, '/Users/jacknosila/.openclaw/workspace/.venv/lib/python3.14/site-packages')

from agentmail import AgentMail

# Load credentials
api_key = "am_us_5bafd5d861e99af53db68dbb8b82c5f5253b501d5727ade866cbebbdb1fd6fc3"
inbox_id = "jacknosila@agentmail.to"

# Initialize client
client = AgentMail(api_key=api_key)

# Get messages
messages = client.inboxes.messages.list(inbox_id=inbox_id, limit=20)

# Filter for unread
unread_messages = []
for msg in messages.messages:
    if 'unread' in msg.labels:
        unread_messages.append({
            'from': msg.from_,
            'subject': msg.subject,
            'message_id': msg.message_id,
            'date': str(msg.created_at),
            'preview': msg.preview[:100] if hasattr(msg, 'preview') and msg.preview else ''
        })

# Output as JSON
print(json.dumps({
    'total_messages': messages.count,
    'unread_count': len(unread_messages),
    'unread_messages': unread_messages
}, indent=2))
