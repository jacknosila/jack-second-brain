#!/usr/bin/env python3
"""
Monitor Aave V3 position health on Ethereum mainnet
Address: 0xA7c87f5FF7367f0b30D376A4aCc2a2eD93624f5b
"""

import requests
import sys

AAVE_ADDRESS = "0xA7c87f5FF7367f0b30D376A4aCc2a2eD93624f5b"
AAVE_V3_POOL = "0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2"  # Ethereum mainnet

def format_usd(value):
    """Format value as USD"""
    if value >= 1_000_000:
        return f"${value/1_000_000:.2f}M"
    elif value >= 1_000:
        return f"${value/1_000:.2f}K"
    else:
        return f"${value:.2f}"

def get_aave_position():
    """
    Query Aave V3 position using Aave API
    Falls back to Etherscan if needed
    """
    try:
        # Try Aave Subgraph API
        url = "https://api.thegraph.com/subgraphs/name/aave/protocol-v3"
        
        query = """
        query getUserData($user: String!) {
          user(id: $user) {
            id
            reserves {
              reserve {
                symbol
                decimals
              }
              currentATokenBalance
              currentTotalDebt
            }
          }
        }
        """
        
        response = requests.post(
            url,
            json={
                "query": query,
                "variables": {"user": AAVE_ADDRESS.lower()}
            },
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            user_data = data.get("data", {}).get("user")
            
            if user_data:
                total_collateral = 0
                total_debt = 0
                
                # Parse reserves
                for reserve in user_data.get("reserves", []):
                    symbol = reserve["reserve"]["symbol"]
                    decimals = int(reserve["reserve"]["decimals"])
                    
                    # Note: Need price data to convert to USD
                    # This is simplified - would need Chainlink price feeds
                    balance = float(reserve.get("currentATokenBalance", 0)) / (10 ** decimals)
                    debt = float(reserve.get("currentTotalDebt", 0)) / (10 ** decimals)
                    
                    print(f"  {symbol}: {balance:.4f} supplied, {debt:.4f} borrowed")
                
                # For now, return placeholder with note
                return {
                    "health_factor": "Query via RPC",
                    "collateral": "Query via RPC", 
                    "debt": "Query via RPC",
                    "note": "Subgraph returned data but needs price conversion"
                }
        
        # Fallback: return status that RPC is needed
        return {
            "health_factor": None,
            "collateral": None,
            "debt": None,
            "note": "Requires Web3 RPC access (Infura/Alchemy)"
        }
        
    except Exception as e:
        return {
            "health_factor": None,
            "collateral": None,
            "debt": None,
            "error": str(e)
        }

def main():
    """Main entry point"""
    position = get_aave_position()
    
    if position.get("error"):
        print(f"❌ Error: {position['error']}")
        return 1
    
    print(f"\n💎 AAVE V3 POSITION")
    print(f"Address: {AAVE_ADDRESS}")
    print()
    
    if position.get("health_factor"):
        print(f"Health Factor: {position['health_factor']}")
        print(f"Collateral: {position['collateral']}")
        print(f"Debt: {position['debt']}")
    else:
        print("⚠️  Position monitoring requires Web3 RPC setup")
        print()
        print("To enable:")
        print("1. Get Infura or Alchemy API key")
        print("2. Add to .credentials/jack.env:")
        print("   WEB3_RPC_URL=https://mainnet.infura.io/v3/YOUR_KEY")
        print("3. Install web3.py: pip3 install web3")
    
    if position.get("note"):
        print(f"\nNote: {position['note']}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
