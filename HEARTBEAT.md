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
- **Do NOT proactively alert about calendar events**
- Only check/report when explicitly asked
- Calendar available for queries: "What's on my calendar today?"
- Track in memory/heartbeat-state.json for reference only
