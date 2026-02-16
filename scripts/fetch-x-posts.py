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

# Accounts to monitor
MONITORED_ACCOUNTS = [
    "mattshumer_",      # AI/ML
    "RichardHeartWin",  # Crypto/Finance
    "DavidDeutschOxf",  # Physics/Philosophy
    "karpathy",         # AI/ML
    "steipete"          # Tech/iOS
]

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
    
    # If all instances fail, return empty
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

def format_tweets_for_briefing(tweets, max_tweets=2):
    """Format top tweets for the daily briefing"""
    
    if not tweets:
        return "  [Unable to fetch posts at this time]\n"
    
    output = ""
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
    
    print(f"\nFound {len(tweets)} tweets")
    print("\nTop 2 most interesting:\n")
    print(format_tweets_for_briefing(tweets, max_tweets=2))
