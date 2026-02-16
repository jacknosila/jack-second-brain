# Google OAuth2 Setup for Gmail & Calendar

## Status
- ⏳ **Pending** - Waiting for app passwords to become available OR OAuth2 setup
- 📧 Gmail account created: jacknosila@gmail.com (approved Feb 16, 2026)
- 🔐 2FA enabled
- ❌ App passwords not yet available (account may be too new)

## Option A: App Passwords (simpler - preferred)
**Wait 10-30 minutes after enabling 2FA, then:**

1. Go to: https://myaccount.google.com/apppasswords
2. If available:
   - App: Mail
   - Device: OpenClaw
   - Copy 16-character password
   - Update `.credentials/jack.env` → `GMAIL_APP_PASSWORD`

## Option B: OAuth2 (works for all accounts)

### 1. Create Google Cloud Project
- Go to: https://console.cloud.google.com/
- Create new project: "Jack OpenClaw"

### 2. Enable APIs
- Enable **Gmail API**
- Enable **Google Calendar API**

### 3. Configure OAuth Consent Screen
- User Type: External
- App name: Jack OpenClaw
- User support email: johnalison@cmu.edu
- Developer contact: johnalison@cmu.edu
- Scopes needed:
  - `https://www.googleapis.com/auth/gmail.readonly`
  - `https://www.googleapis.com/auth/gmail.send`
  - `https://www.googleapis.com/auth/calendar.events` (read + write - John granted edit access)

### 4. Create OAuth Client ID
- Application type: Desktop app
- Name: Jack Desktop Client
- Download JSON credentials → save as `.credentials/google-oauth-client.json`

### 5. Install Google API Client
```bash
pip3 install --upgrade google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### 6. First-time Auth
Run the auth flow (opens browser, John logs in once, grants permissions)
Saves refresh token for future automated access

## What This Enables
- ✅ Read Gmail inbox
- ✅ Send emails from jacknosila@gmail.com
- ✅ Read John's shared calendar
- ✅ Create/modify calendar events when requested
- ✅ Check upcoming events during heartbeats
- ✅ Alert to important meetings
- ✅ Add appointments, block time, schedule tasks

## Next Steps
1. John shares calendar with jacknosila@gmail.com ✅
2. Try app passwords again (if still blocked, do OAuth2)
3. Test calendar access
4. Add calendar checks to heartbeat routine
