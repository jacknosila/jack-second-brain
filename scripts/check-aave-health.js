#!/usr/bin/env node

const { ethers } = require('ethers');

// Aave V3 Pool address on Ethereum mainnet
const AAVE_V3_POOL = '0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2';

// User address
const USER_ADDRESS = '0xA7c87f5FF7367f0b30D376A4aCc2a2eD93624f5b';

// ABI for getUserAccountData function
const POOL_ABI = [
  {
    "inputs": [{"internalType": "address", "name": "user", "type": "address"}],
    "name": "getUserAccountData",
    "outputs": [
      {"internalType": "uint256", "name": "totalCollateralBase", "type": "uint256"},
      {"internalType": "uint256", "name": "totalDebtBase", "type": "uint256"},
      {"internalType": "uint256", "name": "availableBorrowsBase", "type": "uint256"},
      {"internalType": "uint256", "name": "currentLiquidationThreshold", "type": "uint256"},
      {"internalType": "uint256", "name": "ltv", "type": "uint256"},
      {"internalType": "uint256", "name": "healthFactor", "type": "uint256"}
    ],
    "stateMutability": "view",
    "type": "function"
  }
];

async function checkHealth() {
  try {
    // Use public Ethereum RPC (publicnode.com - free, no key required)
    const provider = new ethers.JsonRpcProvider('https://ethereum-rpc.publicnode.com');
    
    // Create contract instance
    const pool = new ethers.Contract(AAVE_V3_POOL, POOL_ABI, provider);
    
    // Get user account data
    const data = await pool.getUserAccountData(USER_ADDRESS);
    
    // Health factor is returned with 18 decimals
    const healthFactor = Number(data.healthFactor) / 1e18;
    const totalCollateral = Number(data.totalCollateralBase) / 1e8; // Base currency has 8 decimals
    const totalDebt = Number(data.totalDebtBase) / 1e8;
    
    console.log(JSON.stringify({
      healthFactor: healthFactor.toFixed(2),
      totalCollateral: totalCollateral.toFixed(2),
      totalDebt: totalDebt.toFixed(2),
      status: healthFactor > 1.5 ? 'healthy' : healthFactor > 1.2 ? 'caution' : 'danger'
    }));
    
  } catch (error) {
    console.error(JSON.stringify({
      error: error.message
    }));
    process.exit(1);
  }
}

checkHealth();
