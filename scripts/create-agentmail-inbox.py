#!/usr/bin/env python3
"""Create an AgentMail inbox for Jack."""

import warnings
warnings.filterwarnings('ignore', category=UserWarning)

import os
from agentmail import AgentMail

# Load API key from env file
api_key = "am_us_5bafd5d861e99af53db68dbb8b82c5f5253b501d5727ade866cbebbdb1fd6fc3"

# Initialize client
client = AgentMail(api_key=api_key)

# Create inbox with auto-generated username
print("Creating inbox...")
inbox = client.inboxes.create()

print(f"✅ Inbox created successfully!")
print(f"Inbox object: {inbox}")
print(f"Attributes: {dir(inbox)}")
