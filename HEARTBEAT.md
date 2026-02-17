# HEARTBEAT.md

## Email Monitoring
Check BOTH email accounts for new unread messages:

**AgentMail** (jacknosila@agentmail.to):
- Use AgentMail API (credentials in .credentials/jack.env)
- Look for messages with 'unread' label

**Gmail** (jacknosila@gmail.com):
- Use IMAP with app password (credentials in .credentials/jack.env)
- Check UNSEEN messages

For both:
- **Process immediately upon finding unread messages**
- Read the full email content
- Determine appropriate action:
  - Reply if it's straightforward
  - Draft response for John's review if complex
  - Take requested action (schedule, research, etc.)
  - Ask John if uncertain
- Track last checked time in memory/heartbeat-state.json

**Processing Guidelines:**
- Emails from John: Read and act on requests
- Reference requests, scheduling: Handle directly
- Important decisions: Draft for review
- Spam/notifications: Ignore or file

Check every 3-4 heartbeats (roughly every 90-120 minutes during day)

## Calendar Monitoring (when OAuth2 set up)
- **Do NOT proactively alert about calendar events**
- Only check/report when explicitly asked
- Calendar available for queries: "What's on my calendar today?"
- Track in memory/heartbeat-state.json for reference only
