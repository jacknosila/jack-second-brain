# HEALTH.md - System Health Checklist

Run this periodically (weekly or after restarts) to verify all systems are operating correctly.

## 1. Cron Jobs
- [ ] Daily briefing scheduled and enabled (7:30 AM EST)
- [ ] Daily commit scheduled and enabled (10 PM EST)
- [ ] Last runs completed successfully
- [ ] Check: `cron list`

## 2. Email Monitoring
- [ ] Gmail IMAP accessible (jacknosila@gmail.com)
- [ ] AgentMail API accessible (jacknosila@agentmail.to)
- [ ] Credentials loaded from `.credentials/jack.env`
- [ ] Last check timestamp in `memory/heartbeat-state.json` is recent
- [ ] Test: Run manual email check

## 3. Git Repository
- [ ] Workspace repo has remote configured
- [ ] No critical uncommitted changes
- [ ] Last push was recent (within 24-48h)
- [ ] Check: `git status`, `git log -1`

## 4. Scripts & Automation
- [ ] `scripts/generate-daily-briefing-v2.py` exists and executable
- [ ] `scripts/send-email.py` exists and executable
- [ ] `scripts/x-top-posts.py` exists and executable
- [ ] Twitter API credentials working (if applicable)

## 5. Memory & Documentation
- [ ] `MEMORY.md` up to date with recent significant events
- [ ] `memory/YYYY-MM-DD.md` exists for today
- [ ] `memory/heartbeat-state.json` tracking correctly

## 6. Gateway
- [ ] Gateway running (`openclaw gateway status`)
- [ ] No errors in recent logs
- [ ] Heartbeat polls arriving regularly (~90-120 min)

## 7. Credentials
- [ ] `.credentials/jack.env` exists and readable
- [ ] Contains: Gmail, AgentMail, GitHub, OpenAI keys
- [ ] Not committed to git (check `.gitignore`)

## Quick Health Check Command
```bash
cd /Users/jacknosila/.openclaw/workspace
echo "=== Cron Jobs ===" && openclaw cron list --includeDisabled
echo -e "\n=== Git Status ===" && git status -sb
echo -e "\n=== Recent Commits ===" && git log -3 --oneline
echo -e "\n=== Scripts ===" && ls -lh scripts/*.py
echo -e "\n=== Memory ===" && ls -lht memory/*.md | head -5
echo -e "\n=== Heartbeat State ===" && cat memory/heartbeat-state.json
```

## Troubleshooting

**Cron jobs not running:**
- Check gateway is running: `openclaw gateway status`
- Verify wake mode is set correctly
- Check isolated session logs

**Email monitoring failing:**
- Verify credentials in `.credentials/jack.env`
- Test Gmail IMAP: `python3 -c "import imaplib; m=imaplib.IMAP4_SSL('imap.gmail.com'); m.login('jacknosila@gmail.com', 'ncdk kvey rymr fhxz'); print('OK')"`
- Check AgentMail API endpoint (currently returning 404)

**Git push failing:**
- Check SSH key: `ssh -T git@github.com`
- Verify remote: `git remote -v`

---
**Last Updated:** 2026-02-17
