#!/usr/bin/env python3
"""
Gmail OAuth2 Setup
This is more involved but works when app passwords aren't available
"""

print("""
Gmail OAuth2 Setup Instructions
================================

Since app passwords aren't available, we'll use OAuth2.

Steps:
1. Go to: https://console.cloud.google.com/
2. Create a new project (or select existing)
3. Enable Gmail API:
   - APIs & Services → Library
   - Search "Gmail API" → Enable
4. Create OAuth credentials:
   - APIs & Services → Credentials
   - Create Credentials → OAuth client ID
   - Application type: Desktop app
   - Name it "Jack OpenClaw"
5. Download JSON credentials file
6. Send me that JSON file

Alternative: Try app passwords again in ~10 minutes
(Sometimes takes time to propagate after enabling 2FA)

Or... we can use AgentMail for now and revisit Gmail later!
""")
