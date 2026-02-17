# Email Configuration

**Updated:** 2026-02-16

## Overview

Jack uses **Gmail as primary** email address with **AgentMail as fallback**.

## Email Accounts

### Primary: Gmail
- **Address:** jacknosila@gmail.com
- **Created:** 2026-02-16 (approved by Google)
- **Authentication:** App Password (in `.credentials/jack.env`)
- **Purpose:** Professional outgoing mail, calendar integration
- **SMTP:** smtp.gmail.com:587

### Fallback: AgentMail
- **Address:** jacknosila@agentmail.to
- **Authentication:** API Key (in `.credentials/jack.env`)
- **Purpose:** Backup sending, inbox monitoring
- **API:** https://api.agentmail.to/v0/

## Sending Email

### Unified Send Script

`scripts/send-email.py` handles all outgoing email with automatic fallback:

```bash
python3 send-email.py <to_address> <subject> <body_file_or_text>
```

**Logic:**
1. Try Gmail SMTP first (professional, reliable)
2. If Gmail fails → fall back to AgentMail API
3. Report which method succeeded

**Example:**
```bash
python3 send-email.py johnda102@gmail.com "Test Subject" /tmp/message.txt
```

### Daily Briefing

The 7 AM daily briefing uses Gmail by default:
- Script: `generate-daily-briefing-v2.py` → `send-email.py`
- Sender: jacknosila@gmail.com
- Recipient: johnda102@gmail.com

## Receiving Email

### AgentMail Inbox Monitoring

Jack checks AgentMail inbox every 60-90 minutes via heartbeat:
- Reads `HEARTBEAT.md` for instructions
- Fetches unread messages via API
- Processes emails immediately (replies, drafts, actions)
- Does NOT just alert—takes action when appropriate

### Gmail Inbox

Gmail is configured but not actively monitored (calendar OAuth only). Could add IMAP monitoring if needed.

## Credentials

All credentials stored in `.credentials/jack.env` (in `.gitignore`):

```bash
# Gmail
GMAIL_EMAIL=jacknosila@gmail.com
GMAIL_PASSWORD=Fiction1@Amusement@Clumsily
GMAIL_APP_PASSWORD="ncdk kvey rymr fhxz"  # Note: quoted (has spaces)

# AgentMail
AGENTMAIL_EMAIL=jacknosila@proton.me
AGENTMAIL_PASSWORD=Recharger6@Liberty@Patriarch
AGENTMAIL_API_KEY=am_us_5bafd5d861e99af53db68dbb8b82c5f5253b501d5727ade866cbebbdb1fd6fc3
AGENTMAIL_INBOX_ID=jacknosila@agentmail.to
```

## Python SDK

AgentMail Python SDK installed globally:
```bash
pip3 install --break-system-packages agentmail
```

## Testing

Test the send script:
```bash
echo "Test message" > /tmp/test.txt
python3 scripts/send-email.py johnda102@gmail.com "Test" /tmp/test.txt
```

Should output:
```
✅ Sent via Gmail (jacknosila@gmail.com)
```

If Gmail fails, you'll see:
```
⚠️  Gmail failed: <error>
⚠️  Falling back to AgentMail...
✅ Sent via AgentMail (fallback) - Message ID: <id>
```

## Future Enhancements

- [ ] Add Gmail IMAP monitoring (in addition to AgentMail)
- [ ] Implement retry logic with exponential backoff
- [ ] Add email templates for common messages
- [ ] Log all sent emails to `memory/email-log.json`
