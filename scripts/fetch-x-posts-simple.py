#!/usr/bin/env python3
"""
Simplified X post fetcher that will be called from OpenClaw
Uses web_search to find recent posts from monitored accounts
"""

MONITORED_ACCOUNTS = [
    "mattshumer_",      # AI/ML
    "RichardHeartWin",  # Crypto/Finance
    "DavidDeutschOxf",  # Physics/Philosophy
    "karpathy",         # AI/ML
    "steipete"          # Tech/iOS
]

def generate_search_queries():
    """Generate search queries for recent posts"""
    queries = []
    for account in MONITORED_ACCOUNTS:
        # Search for recent posts from this account
        query = f"site:twitter.com OR site:x.com @{account}"
        queries.append(query)
    return queries

if __name__ == "__main__":
    print("X Account Monitoring List:")
    print("=" * 50)
    for account in MONITORED_ACCOUNTS:
        print(f"  • @{account}")
    print("\nNote: Fetching will be done via OpenClaw web_search tool")
    print("during briefing generation")
