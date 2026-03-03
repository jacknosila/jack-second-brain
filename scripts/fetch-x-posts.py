#!/usr/bin/env python3
"""
Fetch recent X/Twitter posts from monitored accounts
Uses web scraping since X API requires paid access
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import time
from pathlib import Path

# Cache path
CACHE_PATH = Path.home() / ".openclaw/workspace/memory/briefings/x-cache.json"

# Accounts to monitor
MONITORED_ACCOUNTS = [
    "mattshumer_",      # AI/ML
    "RichardHeartWin",  # Crypto/Finance
    "DavidDeutschOxf",  # Physics/Philosophy
    "karpathy",         # AI/ML
    "steipete"          # Tech/iOS
]

def fetch_user_tweets_jina(username, max_tweets=5):
    """Fallback: fetch via r.jina.ai proxy of X (text-only)"""
    try:
        url = f"https://r.jina.ai/http://x.com/{username}"
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return []
        text = response.text
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        # crude extraction: take first few lines after username occurrences
        tweets = []
        for line in lines:
            if line.startswith("@") or line.startswith(username):
                continue
            if len(line) > 20 and len(tweets) < max_tweets:
                tweets.append({
                    'username': username,
                    'text': line,
                    'timestamp': '',
                    'source': 'jina'
                })
        return tweets[:max_tweets]
    except Exception:
        return []


def fetch_user_tweets_nitter(username, max_tweets=5):
    """
    Fetch tweets using Nitter (privacy-respecting Twitter frontend)
    Nitter provides a simple HTML structure we can parse
    """
    
    # Try multiple Nitter instances (they rotate/go down)
    nitter_instances = [
        "nitter.net",
        "nitter.poast.org",
        "nitter.privacydev.net"
    ]
    
    for instance in nitter_instances:
        try:
            url = f"https://{instance}/{username}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                tweets = []
                tweet_containers = soup.find_all('div', class_='timeline-item', limit=max_tweets)
                
                for container in tweet_containers:
                    # Extract tweet text
                    tweet_content = container.find('div', class_='tweet-content')
                    if tweet_content:
                        text = tweet_content.get_text(strip=True)
                        
                        # Extract timestamp
                        timestamp_elem = container.find('span', class_='tweet-date')
                        timestamp = timestamp_elem.get_text(strip=True) if timestamp_elem else ''
                        
                        tweets.append({
                            'username': username,
                            'text': text,
                            'timestamp': timestamp,
                            'source': instance
                        })
                
                return tweets
                
        except Exception as e:
            print(f"Failed to fetch from {instance}: {e}")
            continue
    
    # If all instances fail, try jina.ai text proxy
    jina = fetch_user_tweets_jina(username, max_tweets=max_tweets)
    if jina:
        return jina

    # If all fail, return empty
    return []

def rank_tweet_interest(tweet):
    """
    Simple scoring system to rank tweet interestingness
    You can customize this based on John's interests
    """
    text = tweet['text'].lower()
    score = 0
    
    # Keywords that indicate interesting content
    interesting_keywords = [
        'breakthrough', 'discovery', 'research', 'paper',
        'physics', 'quantum', 'ai', 'ml', 'llm',
        'launch', 'release', 'open source',
        'higgs', 'particle', 'cms', 'cern', 'lhc'
    ]
    
    for keyword in interesting_keywords:
        if keyword in text:
            score += 1
    
    # Longer tweets often have more substance
    if len(text) > 200:
        score += 1
    
    # Tweets with links might be more informative
    if 'http' in text:
        score += 0.5
    
    return score

def fetch_all_monitored_tweets():
    """Fetch tweets from all monitored accounts and rank them"""
    
    all_tweets = []
    
    for username in MONITORED_ACCOUNTS:
        print(f"Fetching tweets from @{username}...")
        tweets = fetch_user_tweets_nitter(username, max_tweets=3)
        all_tweets.extend(tweets)
        time.sleep(1)  # Be nice to the server
    
    # Rank tweets by interest
    for tweet in all_tweets:
        tweet['interest_score'] = rank_tweet_interest(tweet)
    
    # Sort by interest score
    all_tweets.sort(key=lambda x: x['interest_score'], reverse=True)

    return all_tweets

def load_cache():
    try:
        if CACHE_PATH.exists():
            return json.loads(CACHE_PATH.read_text())
    except Exception:
        return None
    return None


def save_cache(tweets):
    try:
        CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
        CACHE_PATH.write_text(json.dumps({
            "timestamp": datetime.now().isoformat(),
            "tweets": tweets
        }, indent=2))
    except Exception:
        pass


def format_tweets_for_briefing(tweets, max_tweets=2, cached=False, cache_ts=None):
    """Format top tweets for the daily briefing"""
    
    if not tweets:
        return "  [Unable to fetch posts at this time]\n"
    
    output = ""
    if cached and cache_ts:
        output += f"[Using cached posts from {cache_ts}]\n"
    for tweet in tweets[:max_tweets]:
        # Truncate long tweets
        text = tweet['text']
        if len(text) > 200:
            text = text[:197] + "..."
        
        output += f"\n@{tweet['username']}\n"
        output += f'  "{text}"\n'
        output += f"  {tweet['timestamp']}\n"
    
    return output

if __name__ == "__main__":
    print("Fetching recent posts from monitored X accounts...\n")
    tweets = fetch_all_monitored_tweets()

    cached = False
    cache_ts = None
    if tweets:
        save_cache(tweets)
    else:
        cache = load_cache()
        if cache and cache.get("tweets"):
            tweets = cache.get("tweets")
            cached = True
            cache_ts = cache.get("timestamp")

    print(f"\nFound {len(tweets)} tweets")
    print("\nTop 2 most interesting:\n")
    print(format_tweets_for_briefing(tweets, max_tweets=2, cached=cached, cache_ts=cache_ts))
