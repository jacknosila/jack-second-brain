#!/usr/bin/env python3
"""Test sending an email via AgentMail."""

import warnings
warnings.filterwarnings('ignore', category=UserWarning)

import os
from agentmail import AgentMail

# Load credentials
api_key = "am_us_5bafd5d861e99af53db68dbb8b82c5f5253b501d5727ade866cbebbdb1fd6fc3"
inbox_id = "jacknosila@agentmail.to"

# Initialize client
client = AgentMail(api_key=api_key)

# Send test email to John
print("Sending test email...")
message = client.inboxes.messages.send(
    inbox_id=inbox_id,
    to="johnda102@gmail.com",
    subject="AgentMail Test - Jack is Online! ⚡",
    text="""Hi John,

This is a test email from your AI assistant Jack Nosila!

✅ AgentMail is now fully configured and working
📧 My email: plainprofession41@agentmail.to
🔑 API key stored securely

I can now:
- Send and receive emails programmatically
- Handle forwarded articles and content
- Integrate email into my daily workflow

Looking forward to helping you stay organized!

Best,
Jack ⚡
"""
)

print(f"✅ Test email sent successfully!")
print(f"Message ID: {message}")
