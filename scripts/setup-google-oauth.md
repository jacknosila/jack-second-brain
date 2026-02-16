# Google OAuth2 Setup - Step by Step

## Quick Setup (15 minutes)

### Step 1: Create Google Cloud Project
1. Go to: https://console.cloud.google.com/
2. Sign in as **jacknosila@gmail.com**
3. Click "Select a project" → "New Project"
4. Name: "Jack OpenClaw"
5. Click "Create"

### Step 2: Enable Google Calendar API
1. In the project, go to: "APIs & Services" → "Library"
2. Search: "Google Calendar API"
3. Click it → Click "Enable"

### Step 3: Configure OAuth Consent Screen
1. Go to: "APIs & Services" → "OAuth consent screen"
2. User Type: **External** → Click "Create"
3. Fill in:
   - App name: `Jack OpenClaw`
   - User support email: `johnalison@cmu.edu`
   - Developer contact: `johnalison@cmu.edu`
4. Click "Save and Continue"
5. Scopes: Click "Add or Remove Scopes"
   - Search and add: `calendar.events` (full calendar access)
   - Click "Update" → "Save and Continue"
6. Test users: Click "Add Users"
   - Add: `jacknosila@gmail.com`
   - Click "Save and Continue"
7. Click "Back to Dashboard"

### Step 4: Create OAuth Client ID
1. Go to: "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth client ID"
3. Application type: **Desktop app**
4. Name: `Jack Desktop Client`
5. Click "Create"
6. **Download JSON** → save as `google-oauth-credentials.json`
7. Upload that file to me (or paste the contents)

### Step 5: I'll handle the rest
Once I have the credentials JSON, I'll:
- Run the initial auth flow (opens browser on your Mac)
- You log in as jacknosila@gmail.com and grant permissions
- Accept the calendar invitation
- Add the "go home" event at 1:15 PM today

---

## Ready?
Follow steps 1-4, then send me the `google-oauth-credentials.json` file!
