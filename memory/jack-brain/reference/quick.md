# Quick Reference

## Emergency Commands

```bash
# Check OpenClaw status
openclaw status

# Restart gateway
openclaw gateway restart

# View logs
tail -f ~/.openclaw/logs/gateway.log
```

## File Locations

- **Workspace**: `/Users/jacknosila/.openclaw/workspace`
- **Config**: `~/.openclaw/openclaw.json`
- **Logs**: `~/.openclaw/logs/`
- **Scripts**: `~/jack/.openclaw/workspace/scripts/`

## Cron Job IDs

- **Daily Briefing**: `3a73deb3-d9f8-4fc0-95b5-f15ea5b62291`

## Important Addresses

- **John's Aave V3**: `0xA7c87f5FF7367f0b30D376A4aCc2a2eD93624f5b`

## API Keys

- **Brave Search**: Stored in `tools.web.search.apiKey`
- **Anthropic**: Auto-managed via OpenClaw

## Contact Info

- **John's Telegram**: `7748852239`
- **Timezone**: EST (America/New_York)

## Session Types

- **Main session**: Direct chats with John
- **Isolated session**: Background tasks, cron jobs
- **Subagent**: Spawned for complex work

## Daily Routine

1. **7:30 AM EST**: Daily briefing fires
2. **As needed**: Heartbeat checks (currently empty)
3. **End of day**: Update memory files

## Common Pitfalls

- ❌ Don't commit node_modules
- ❌ Don't use placeholder values in scripts
- ❌ Don't skip testing before deployment
- ❌ Don't read MEMORY.md in group chats
- ✅ Do write things down (files > mental notes)
- ✅ Do test everything
- ✅ Do verify external data
- ✅ Do commit regularly

---

_Last updated: 2026-02-15_
