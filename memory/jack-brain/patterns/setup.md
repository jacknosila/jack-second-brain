# System Setup Patterns

## Daily Briefing Setup

**Pattern**: Isolated session with announce delivery

```javascript
{
  "name": "Daily Summary",
  "schedule": {
    "kind": "cron",
    "expr": "30 7 * * *",
    "tz": "America/New_York"
  },
  "payload": {
    "kind": "agentTurn",
    "message": "<briefing instructions>",
    "timeoutSeconds": 120
  },
  "delivery": {
    "mode": "announce",
    "channel": "telegram",
    "to": "<user-id>"
  },
  "sessionTarget": "isolated",
  "enabled": true
}
```

**Key learnings**:
- Use `isolated` for background tasks
- `announce` mode delivers directly to channel
- `cron` with timezone for precise scheduling
- Test with `cron run <job-id>` before enabling

## Blockchain Monitoring

**Pattern**: Direct RPC queries with ethers.js

```javascript
const { ethers } = require('ethers');

// Use public RPC (no auth)
const provider = new ethers.JsonRpcProvider('https://ethereum-rpc.publicnode.com');

// Read-only contract calls
const contract = new ethers.Contract(address, abi, provider);
const data = await contract.method();
```

**Key learnings**:
- Public RPCs work for read-only operations
- No API keys needed (simpler, more reliable)
- Always verify against canonical sources (dashboards)
- Format numbers carefully (wei → ether, precision)

## Git Workspace Tracking

**Pattern**: Version control for persistence

```bash
# Initialize
git init
git add AGENTS.md SOUL.md USER.md IDENTITY.md TOOLS.md HEARTBEAT.md

# Always ignore dependencies
echo "node_modules/" >> .gitignore
echo ".DS_Store" >> .gitignore

# Regular commits
git add -A
git commit -m "Descriptive message"
```

**Key learnings**:
- Track workspace files for continuity
- Exclude large dependencies (node_modules)
- Commit frequently with clear messages
- `.gitignore` saves massive headaches

## OpenClaw Config Changes

**Pattern**: Use gateway tools when possible

```bash
# Get current config
gateway config.get

# Get schema for reference
gateway config.schema

# Apply changes
gateway config.patch {...}
```

**Key learnings**:
- Schema is authoritative (18k+ lines)
- `config.patch` merges safely
- Always include `note` parameter for restart messages
- Some changes require restart

## Web Search Setup

**Pattern**: API key in config, tier-appropriate usage

```json
{
  "tools": {
    "web": {
      "search": {
        "apiKey": "<brave-api-key>",
        "provider": "brave",
        "maxResults": 3
      }
    }
  }
}
```

**Key learnings**:
- Free tier has rate limits
- Tier upgrades unlock full functionality
- Test with `web_search` tool after setup
- Fallback: `web_fetch` for lightweight scraping

---

_Last updated: 2026-02-15_
