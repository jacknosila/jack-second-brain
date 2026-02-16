# HEARTBEAT.md

## Email Monitoring
Check jacknosila@agentmail.to for new unread messages:
- Use AgentMail API (credentials in .credentials/jack.env)
- Look for messages with 'unread' label
- If found, read and decide if immediate response needed
- Reply thoughtfully to emails from John
- Track last checked time in memory/heartbeat-state.json

Check every 2-3 heartbeats (roughly every 60-90 minutes during day)

## Calendar Monitoring (when OAuth2 set up)
Check John's shared Google Calendar for upcoming events:
- Events in next 2 hours → alert immediately
- Events today → mention in morning/midday checks
- Events tomorrow → mention in evening check
- Track in memory/heartbeat-state.json
