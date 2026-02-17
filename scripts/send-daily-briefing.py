#!/usr/bin/env python3
"""Send daily briefing email via AgentMail."""

import sys
import os

# Add the venv to the path
sys.path.insert(0, '/Users/jacknosila/.openclaw/workspace/.venv/lib/python3.14/site-packages')

import warnings
warnings.filterwarnings('ignore', category=UserWarning)

from agentmail import AgentMail

# Load credentials
api_key = "am_us_5bafd5d861e99af53db68dbb8b82c5f5253b501d5727ade866cbebbdb1fd6fc3"
inbox_id = "jacknosila@agentmail.to"

# Get briefing content from stdin or args
if len(sys.argv) > 1:
    briefing_text = sys.argv[1]
else:
    briefing_text = sys.stdin.read()

# Get subject (default if not provided)
subject = sys.argv[2] if len(sys.argv) > 2 else "Daily Briefing"

# Initialize client
client = AgentMail(api_key=api_key)

# Send email
message = client.inboxes.messages.send(
    inbox_id=inbox_id,
    to="johnda102@gmail.com",
    subject=subject,
    text=briefing_text
)

print(f"✅ Email sent! Message ID: {message.message_id}")
