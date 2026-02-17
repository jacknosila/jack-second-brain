# Setup Data Sources for Daily Briefing

To get real data in your daily briefing (not placeholders), we need API access for:

## 1. Aave V3 Position Monitoring ✅ READY TO FIX

**Your Address:** `0xA7c87f5FF7367f0b30D376A4aCc2a2eD93624f5b`

**What's needed:**
- Ethereum RPC provider (Infura or Alchemy)
- Both have free tiers that work fine

**Setup Steps:**

### Option A: Infura (Recommended - simpler)
1. Sign up at https://infura.io/
2. Create a new project
3. Copy your Ethereum mainnet endpoint
4. Add to `.credentials/jack.env`:
   ```bash
   WEB3_RPC_URL=https://mainnet.infura.io/v3/YOUR_PROJECT_ID
   ```

### Option B: Alchemy
1. Sign up at https://www.alchemy.com/
2. Create app (Ethereum Mainnet)
3. Copy HTTPS endpoint
4. Add to `.credentials/jack.env`:
   ```bash
   WEB3_RPC_URL=https://eth-mainnet.g.alchemy.com/v2/YOUR_API_KEY
   ```

### After adding RPC:
```bash
pip3 install web3
python3 scripts/aave-monitor.py  # Test it works
```

**What you'll get:**
- Real-time health factor
- Total collateral in USD
- Total debt in USD
- Liquidation risk warnings if health factor < 1.5

---

## 2. X/Twitter Posts ⏳ WAITING ON API KEY

**Accounts monitored:**
- @mattshumer_
- @RichardHeartWin
- @DavidDeutschOxf
- @karpathy
- @steipete

**What's needed:**
- X API v2 access (requires X Developer account)

**Setup Steps:**
1. Apply for X Developer account: https://developer.twitter.com/
2. Create a project and app
3. Get your Bearer Token
4. Add to `.credentials/jack.env`:
   ```bash
   X_API_BEARER_TOKEN=your_bearer_token_here
   ```

### Alternative: Web Scraping (if API denied)
If X API access is denied/expensive, I can implement web scraping using:
- Playwright/Selenium
- Or nitter instances
- Less reliable but free

**What you'll get:**
- Top 1-2 most interesting/engaged posts from last 24h
- Direct links to posts
- Brief context/summary

---

## Priority

**Do first:** Aave monitoring (5 min setup, free tier works)
**Do when ready:** X API (requires approval, may take time)

---

## Current Status

- ✅ Weather: Working (wttr.in API)
- ❌ Aave: Needs RPC setup
- ❌ X Posts: Needs API key
- ✅ Book Insights: Working

Let me know when you've set up Infura/Alchemy and I'll implement the full Aave monitoring!
