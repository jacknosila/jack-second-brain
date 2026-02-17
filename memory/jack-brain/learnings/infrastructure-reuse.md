# Infrastructure Reuse - Don't Rebuild What Exists

**Date**: 2026-02-17  
**Context**: Daily briefing Aave monitoring issue  
**Lesson**: Use existing infrastructure before building new

## The Mistake

When asked to add real Aave data to the daily briefing, I:

1. **First attempt**: Started building `aave-monitor.py` from scratch
   - Created new Python script with web3 integration
   - Wrote setup documentation for API keys
   - Wasted time building something new

2. **Second attempt**: Used cached static data
   - Found old numbers in john.md: HF 2.05, $360k/$142k
   - But these change DAILY with crypto prices!
   - Static cache is useless for live financial data

3. **Correct approach**: Found existing `check-aave-health.js`
   - Already working from Feb 15 commit
   - Uses ethers.js + free public RPC
   - Just needed to be integrated, not rebuilt

## The Principle

**Before building new infrastructure:**

1. **Search existing code**
   ```bash
   # Search for existing scripts
   find . -name "*.js" -o -name "*.py" | xargs grep -l "aave\|defi"
   
   # Search git history
   git log --all --oneline --grep="aave\|defi" -i
   
   # Search for similar functionality
   ls scripts/check-* scripts/*-health.* scripts/*-monitor.*
   ```

2. **Check what already works**
   - Don't assume you need new dependencies
   - Don't assume you need new API keys
   - Test what exists first

3. **Build only what's missing**
   - If existing code does 80%, extend it
   - Don't rewrite from scratch

## Technical Details

### Existing Aave Monitoring Stack (Feb 15, 2026)

**Location**: `scripts/check-aave-health.js`

**Dependencies** (already installed):
- ethers.js
- Node.js

**How it works**:
```javascript
// Uses free public RPC - no API key needed
const provider = new ethers.JsonRpcProvider('https://ethereum-rpc.publicnode.com');

// Queries Aave V3 Pool contract
const pool = new ethers.Contract(AAVE_V3_POOL, POOL_ABI, provider);
const data = await pool.getUserAccountData(USER_ADDRESS);

// Returns: healthFactor, totalCollateral, totalDebt
```

**Integration**:
```python
# In generate-daily-briefing-v2.py
result = subprocess.run(['node', 'check-aave-health.js'], 
                       capture_output=True, text=True)
data = json.loads(result.stdout)
```

**No setup required** - works out of the box!

## When to Build New vs Reuse

### Reuse existing when:
- ✅ It solves the problem (even if not perfect)
- ✅ It's maintained and working
- ✅ Integration cost is low
- ✅ It has all necessary dependencies

### Build new when:
- ❌ Existing solution is fundamentally broken
- ❌ Requirements are completely different
- ❌ Existing code is deprecated/unmaintained
- ❌ Integration is more complex than rewriting

## Search Commands Cheatsheet

```bash
# Find Python scripts
find . -name "*.py" -type f | grep -v __pycache__

# Find JS scripts  
find . -name "*.js" -type f

# Search file contents
grep -r "keyword" --include="*.py" --include="*.js"

# Search git history
git log --all --oneline --grep="keyword" -i
git log --all --oneline --since="2026-02-01" -- "*.js"

# Show old file version
git show COMMIT_HASH:path/to/file

# Search second brain
grep -r "keyword" memory/jack-brain/
```

## Cost of Not Checking First

**Time wasted**: ~30 minutes building duplicate infrastructure  
**Complexity added**: New scripts, new docs, new dependencies  
**Maintenance burden**: Now have two ways to do the same thing  

**Correct approach saved**:
- Used existing working code
- No new dependencies
- No new documentation needed
- Worked immediately

## Remember

> "The best code is no code at all. The second best is code you already wrote that works."

Always check first:
1. `scripts/` directory
2. Git history
3. Second brain docs
4. Then build new if truly needed
