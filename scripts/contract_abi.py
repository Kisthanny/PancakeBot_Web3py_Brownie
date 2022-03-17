false = False
true = True
IFO_3_1 = [
    {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "tokenAddress",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amountTokens",
                "type": "uint256",
            },
        ],
        "name": "AdminTokenRecovery",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amountLP",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amountOfferingToken",
                "type": "uint256",
            },
        ],
        "name": "AdminWithdraw",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
            {"indexed": true, "internalType": "uint8", "name": "pid", "type": "uint8"},
        ],
        "name": "Deposit",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "offeringAmount",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "excessAmount",
                "type": "uint256",
            },
            {"indexed": true, "internalType": "uint8", "name": "pid", "type": "uint8"},
        ],
        "name": "Harvest",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "startBlock",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "endBlock",
                "type": "uint256",
            },
        ],
        "name": "NewStartAndEndBlocks",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "campaignId",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "numberPoints",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "thresholdPoints",
                "type": "uint256",
            },
        ],
        "name": "PointParametersSet",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "offeringAmountPool",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "raisingAmountPool",
                "type": "uint256",
            },
            {"indexed": false, "internalType": "uint8", "name": "pid", "type": "uint8"},
        ],
        "name": "PoolParametersSet",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "_user",
                "type": "address",
            }
        ],
        "name": "WhitelistedAddressAdded",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "_user",
                "type": "address",
            }
        ],
        "name": "WhitelistedAddressRemoved",
        "type": "event",
    },
    {
        "inputs": [],
        "name": "IFO_FACTORY",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "MAX_BUFFER_BLOCKS",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "NUMBER_POOLS",
        "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_user", "type": "address"}],
        "name": "addAddressToWhitelist",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address[]", "name": "_users", "type": "address[]"}
        ],
        "name": "addAddressesToWhitelist",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "admissionProfile",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "campaignId",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            {"internalType": "uint8", "name": "_pid", "type": "uint8"},
        ],
        "name": "depositPool",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "endBlock",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_lpAmount", "type": "uint256"},
            {"internalType": "uint256", "name": "_offerAmount", "type": "uint256"},
        ],
        "name": "finalWithdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint8", "name": "_pid", "type": "uint8"}],
        "name": "harvestPool",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "ifoPool",
        "outputs": [
            {"internalType": "contract IFOPool", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_lpToken", "type": "address"},
            {"internalType": "address", "name": "_offeringToken", "type": "address"},
            {
                "internalType": "address",
                "name": "_pancakeProfileAddress",
                "type": "address",
            },
            {"internalType": "uint256", "name": "_startBlock", "type": "uint256"},
            {"internalType": "uint256", "name": "_endBlock", "type": "uint256"},
            {"internalType": "uint256", "name": "_maxBufferBlocks", "type": "uint256"},
            {"internalType": "address", "name": "_adminAddress", "type": "address"},
            {"internalType": "address", "name": "_ifoPoolAddress", "type": "address"},
            {"internalType": "uint256", "name": "_pointThreshold", "type": "uint256"},
            {"internalType": "address", "name": "_admissionProfile", "type": "address"},
        ],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "isInitialized",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_user", "type": "address"}],
        "name": "isQualifiedNFT",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_user", "type": "address"}],
        "name": "isQualifiedPoints",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_user", "type": "address"}],
        "name": "isQualifiedWhitelist",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_user", "type": "address"}],
        "name": "isWhitelisted",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "lpToken",
        "outputs": [{"internalType": "contract IERC20", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "numberPoints",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "offeringToken",
        "outputs": [{"internalType": "contract IERC20", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "pancakeProfile",
        "outputs": [
            {"internalType": "contract PancakeProfile", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "pointThreshold",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_tokenAddress", "type": "address"},
            {"internalType": "uint256", "name": "_tokenAmount", "type": "uint256"},
        ],
        "name": "recoverWrongTokens",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_user", "type": "address"}],
        "name": "removeAddressFromWhitelist",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address[]", "name": "_users", "type": "address[]"}
        ],
        "name": "removeAddressesFromWhitelist",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_offeringAmountPool",
                "type": "uint256",
            },
            {
                "internalType": "uint256",
                "name": "_raisingAmountPool",
                "type": "uint256",
            },
            {"internalType": "uint256", "name": "_limitPerUserInLP", "type": "uint256"},
            {"internalType": "bool", "name": "_hasTax", "type": "bool"},
            {"internalType": "uint8", "name": "_pid", "type": "uint8"},
            {"internalType": "bool", "name": "_isSpecialSale", "type": "bool"},
        ],
        "name": "setPool",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "startBlock",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "thresholdPoints",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "name": "tokenIdUsed",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "totalTokensOffered",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_campaignId", "type": "uint256"},
            {"internalType": "uint256", "name": "_numberPoints", "type": "uint256"},
            {"internalType": "uint256", "name": "_thresholdPoints", "type": "uint256"},
        ],
        "name": "updatePointParameters",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_startBlock", "type": "uint256"},
            {"internalType": "uint256", "name": "_endBlock", "type": "uint256"},
        ],
        "name": "updateStartAndEndBlocks",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "userCreditUsed",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_pid", "type": "uint256"}],
        "name": "viewPoolInformation",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "bool", "name": "", "type": "bool"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "bool", "name": "", "type": "bool"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_pid", "type": "uint256"}],
        "name": "viewPoolTaxRateOverflow",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_user", "type": "address"},
            {"internalType": "uint8[]", "name": "_pids", "type": "uint8[]"},
        ],
        "name": "viewUserAllocationPools",
        "outputs": [{"internalType": "uint256[]", "name": "", "type": "uint256[]"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_user", "type": "address"},
            {"internalType": "uint8[]", "name": "_pids", "type": "uint8[]"},
        ],
        "name": "viewUserInfo",
        "outputs": [
            {"internalType": "uint256[]", "name": "", "type": "uint256[]"},
            {"internalType": "bool[]", "name": "", "type": "bool[]"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_user", "type": "address"},
            {"internalType": "uint8[]", "name": "_pids", "type": "uint8[]"},
        ],
        "name": "viewUserOfferingAndRefundingAmountsForPools",
        "outputs": [
            {"internalType": "uint256[3][]", "name": "", "type": "uint256[3][]"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
]
SYRUP_POOL = [
    {
        "inputs": [
            {"internalType": "address", "name": "_pancakeProfile", "type": "address"},
            {
                "internalType": "bool",
                "name": "_pancakeProfileIsRequested",
                "type": "bool",
            },
            {
                "internalType": "uint256",
                "name": "_pancakeProfileThresholdPoints",
                "type": "uint256",
            },
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "Deposit",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "EmergencyWithdraw",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "poolLimitPerUser",
                "type": "uint256",
            }
        ],
        "name": "NewPoolLimit",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "rewardPerBlock",
                "type": "uint256",
            }
        ],
        "name": "NewRewardPerBlock",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "startBlock",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "endBlock",
                "type": "uint256",
            },
        ],
        "name": "NewStartAndEndBlocks",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "blockNumber",
                "type": "uint256",
            }
        ],
        "name": "RewardsStop",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "token",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "TokenRecovery",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "bool",
                "name": "isProfileRequested",
                "type": "bool",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "thresholdPoints",
                "type": "uint256",
            },
        ],
        "name": "UpdateProfileAndThresholdPointsRequirement",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "Withdraw",
        "type": "event",
    },
    {
        "inputs": [],
        "name": "PRECISION_FACTOR",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "SMART_CHEF_FACTORY",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "accTokenPerShare",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "bonusEndBlock",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_amount", "type": "uint256"}],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_amount", "type": "uint256"}],
        "name": "emergencyRewardWithdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "emergencyWithdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "hasUserLimit",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract IERC20Metadata",
                "name": "_stakedToken",
                "type": "address",
            },
            {
                "internalType": "contract IERC20Metadata",
                "name": "_rewardToken",
                "type": "address",
            },
            {"internalType": "uint256", "name": "_rewardPerBlock", "type": "uint256"},
            {"internalType": "uint256", "name": "_startBlock", "type": "uint256"},
            {"internalType": "uint256", "name": "_bonusEndBlock", "type": "uint256"},
            {"internalType": "uint256", "name": "_poolLimitPerUser", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "_numberBlocksForUserLimit",
                "type": "uint256",
            },
            {"internalType": "address", "name": "_admin", "type": "address"},
        ],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "isInitialized",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "lastRewardBlock",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "numberBlocksForUserLimit",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "pancakeProfile",
        "outputs": [
            {"internalType": "contract IPancakeProfile", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "pancakeProfileIsRequested",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "pancakeProfileThresholdPoints",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_user", "type": "address"}],
        "name": "pendingReward",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "poolLimitPerUser",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_token", "type": "address"}],
        "name": "recoverToken",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "rewardPerBlock",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "rewardToken",
        "outputs": [
            {"internalType": "contract IERC20Metadata", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "stakedToken",
        "outputs": [
            {"internalType": "contract IERC20Metadata", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "startBlock",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "stopReward",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bool", "name": "_userLimit", "type": "bool"},
            {"internalType": "uint256", "name": "_poolLimitPerUser", "type": "uint256"},
        ],
        "name": "updatePoolLimitPerUser",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bool", "name": "_isRequested", "type": "bool"},
            {"internalType": "uint256", "name": "_thresholdPoints", "type": "uint256"},
        ],
        "name": "updateProfileAndThresholdPointsRequirement",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_rewardPerBlock", "type": "uint256"}
        ],
        "name": "updateRewardPerBlock",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_startBlock", "type": "uint256"},
            {"internalType": "uint256", "name": "_bonusEndBlock", "type": "uint256"},
        ],
        "name": "updateStartAndEndBlocks",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "userInfo",
        "outputs": [
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "uint256", "name": "rewardDebt", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "userLimit",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_amount", "type": "uint256"}],
        "name": "withdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

PANCAKE = [
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "owner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "spender",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
            },
        ],
        "name": "Approval",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "delegator",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "fromDelegate",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "toDelegate",
                "type": "address",
            },
        ],
        "name": "DelegateChanged",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "delegate",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "previousBalance",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "newBalance",
                "type": "uint256",
            },
        ],
        "name": "DelegateVotesChanged",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "from",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "to",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
            },
        ],
        "name": "Transfer",
        "type": "event",
    },
    {
        "inputs": [],
        "name": "DELEGATION_TYPEHASH",
        "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "DOMAIN_TYPEHASH",
        "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "owner", "type": "address"},
            {"internalType": "address", "name": "spender", "type": "address"},
        ],
        "name": "allowance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "approve",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "uint32", "name": "", "type": "uint32"},
        ],
        "name": "checkpoints",
        "outputs": [
            {"internalType": "uint32", "name": "fromBlock", "type": "uint32"},
            {"internalType": "uint256", "name": "votes", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "decimals",
        "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "subtractedValue", "type": "uint256"},
        ],
        "name": "decreaseAllowance",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "delegatee", "type": "address"}],
        "name": "delegate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "delegatee", "type": "address"},
            {"internalType": "uint256", "name": "nonce", "type": "uint256"},
            {"internalType": "uint256", "name": "expiry", "type": "uint256"},
            {"internalType": "uint8", "name": "v", "type": "uint8"},
            {"internalType": "bytes32", "name": "r", "type": "bytes32"},
            {"internalType": "bytes32", "name": "s", "type": "bytes32"},
        ],
        "name": "delegateBySig",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "delegator", "type": "address"}],
        "name": "delegates",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "getCurrentVotes",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getOwner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "uint256", "name": "blockNumber", "type": "uint256"},
        ],
        "name": "getPriorVotes",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "addedValue", "type": "uint256"},
        ],
        "name": "increaseAllowance",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_to", "type": "address"},
            {"internalType": "uint256", "name": "_amount", "type": "uint256"},
        ],
        "name": "mint",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "mint",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "nonces",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "numCheckpoints",
        "outputs": [{"internalType": "uint32", "name": "", "type": "uint32"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "sender", "type": "address"},
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "transferFrom",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]
ERA7 = [
    {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "owner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "spender",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
            },
        ],
        "name": "Approval",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "from",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "to",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
            },
        ],
        "name": "Transfer",
        "type": "event",
    },
    {
        "inputs": [{"internalType": "address", "name": "helper", "type": "address"}],
        "name": "addHelper",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "owner", "type": "address"},
            {"internalType": "address", "name": "spender", "type": "address"},
        ],
        "name": "allowance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "approve",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "burn",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "burnFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "decimals",
        "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "subtractedValue", "type": "uint256"},
        ],
        "name": "decreaseAllowance",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "name": "helpers",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "addedValue", "type": "uint256"},
        ],
        "name": "increaseAllowance",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "maxMint",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "mint",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "pause",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "pauseContract",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "helper", "type": "address"}],
        "name": "removeHelper",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "resume",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "sender", "type": "address"},
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "transferFrom",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]
POOL_TOKEN = [
    {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "owner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "spender",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
            },
        ],
        "name": "Approval",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "from",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "to",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
            },
        ],
        "name": "Transfer",
        "type": "event",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "owner", "type": "address"},
            {"internalType": "address", "name": "spender", "type": "address"},
        ],
        "name": "allowance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "approve",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "burn",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "decimals",
        "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "subtractedValue", "type": "uint256"},
        ],
        "name": "decreaseAllowance",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getOwner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "addedValue", "type": "uint256"},
        ],
        "name": "increaseAllowance",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "string", "name": "name", "type": "string"},
            {"internalType": "string", "name": "symbol", "type": "string"},
            {"internalType": "uint8", "name": "decimals", "type": "uint8"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "bool", "name": "mintable", "type": "bool"},
            {"internalType": "address", "name": "owner", "type": "address"},
        ],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "mint",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "mintable",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "sender", "type": "address"},
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "transferFrom",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

MANUAL_CAKE = [
    {
        "inputs": [
            {"internalType": "contract CakeToken", "name": "_cake", "type": "address"},
            {"internalType": "contract SyrupBar", "name": "_syrup", "type": "address"},
            {"internalType": "address", "name": "_devaddr", "type": "address"},
            {"internalType": "uint256", "name": "_cakePerBlock", "type": "uint256"},
            {"internalType": "uint256", "name": "_startBlock", "type": "uint256"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "pid",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "Deposit",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "pid",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "EmergencyWithdraw",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "pid",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "Withdraw",
        "type": "event",
    },
    {
        "inputs": [],
        "name": "BONUS_MULTIPLIER",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_allocPoint", "type": "uint256"},
            {"internalType": "contract IBEP20", "name": "_lpToken", "type": "address"},
            {"internalType": "bool", "name": "_withUpdate", "type": "bool"},
        ],
        "name": "add",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "cake",
        "outputs": [
            {"internalType": "contract CakeToken", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "cakePerBlock",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_pid", "type": "uint256"},
            {"internalType": "uint256", "name": "_amount", "type": "uint256"},
        ],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_devaddr", "type": "address"}],
        "name": "dev",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "devaddr",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_pid", "type": "uint256"}],
        "name": "emergencyWithdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_amount", "type": "uint256"}],
        "name": "enterStaking",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_from", "type": "uint256"},
            {"internalType": "uint256", "name": "_to", "type": "uint256"},
        ],
        "name": "getMultiplier",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_amount", "type": "uint256"}],
        "name": "leaveStaking",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "massUpdatePools",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_pid", "type": "uint256"}],
        "name": "migrate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "migrator",
        "outputs": [
            {"internalType": "contract IMigratorChef", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_pid", "type": "uint256"},
            {"internalType": "address", "name": "_user", "type": "address"},
        ],
        "name": "pendingCake",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "name": "poolInfo",
        "outputs": [
            {"internalType": "contract IBEP20", "name": "lpToken", "type": "address"},
            {"internalType": "uint256", "name": "allocPoint", "type": "uint256"},
            {"internalType": "uint256", "name": "lastRewardBlock", "type": "uint256"},
            {"internalType": "uint256", "name": "accCakePerShare", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "poolLength",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_pid", "type": "uint256"},
            {"internalType": "uint256", "name": "_allocPoint", "type": "uint256"},
            {"internalType": "bool", "name": "_withUpdate", "type": "bool"},
        ],
        "name": "set",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract IMigratorChef",
                "name": "_migrator",
                "type": "address",
            }
        ],
        "name": "setMigrator",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "startBlock",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "syrup",
        "outputs": [
            {"internalType": "contract SyrupBar", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "totalAllocPoint",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "multiplierNumber", "type": "uint256"}
        ],
        "name": "updateMultiplier",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_pid", "type": "uint256"}],
        "name": "updatePool",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "address", "name": "", "type": "address"},
        ],
        "name": "userInfo",
        "outputs": [
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "uint256", "name": "rewardDebt", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_pid", "type": "uint256"},
            {"internalType": "uint256", "name": "_amount", "type": "uint256"},
        ],
        "name": "withdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

AUTO_CAKE = [
    {
        "inputs": [
            {"internalType": "contract IERC20", "name": "_token", "type": "address"},
            {
                "internalType": "contract IERC20",
                "name": "_receiptToken",
                "type": "address",
            },
            {
                "internalType": "contract IMasterChef",
                "name": "_masterchef",
                "type": "address",
            },
            {"internalType": "address", "name": "_admin", "type": "address"},
            {"internalType": "address", "name": "_treasury", "type": "address"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "shares",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "lastDepositedTime",
                "type": "uint256",
            },
        ],
        "name": "Deposit",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "performanceFee",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "callFee",
                "type": "uint256",
            },
        ],
        "name": "Harvest",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {"anonymous": false, "inputs": [], "name": "Pause", "type": "event"},
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "account",
                "type": "address",
            }
        ],
        "name": "Paused",
        "type": "event",
    },
    {"anonymous": false, "inputs": [], "name": "Unpause", "type": "event"},
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "account",
                "type": "address",
            }
        ],
        "name": "Unpaused",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "shares",
                "type": "uint256",
            },
        ],
        "name": "Withdraw",
        "type": "event",
    },
    {
        "inputs": [],
        "name": "MAX_CALL_FEE",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "MAX_PERFORMANCE_FEE",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "MAX_WITHDRAW_FEE",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "MAX_WITHDRAW_FEE_PERIOD",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "admin",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "available",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "calculateHarvestCakeRewards",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "calculateTotalPendingCakeRewards",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "callFee",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_amount", "type": "uint256"}],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "emergencyWithdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getPricePerFullShare",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "harvest",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_token", "type": "address"}],
        "name": "inCaseTokensGetStuck",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "lastHarvestedTime",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "masterchef",
        "outputs": [
            {"internalType": "contract IMasterChef", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "pause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "paused",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "performanceFee",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "receiptToken",
        "outputs": [{"internalType": "contract IERC20", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_admin", "type": "address"}],
        "name": "setAdmin",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_callFee", "type": "uint256"}],
        "name": "setCallFee",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_performanceFee", "type": "uint256"}
        ],
        "name": "setPerformanceFee",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_treasury", "type": "address"}],
        "name": "setTreasury",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_withdrawFee", "type": "uint256"}
        ],
        "name": "setWithdrawFee",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_withdrawFeePeriod", "type": "uint256"}
        ],
        "name": "setWithdrawFeePeriod",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "token",
        "outputs": [{"internalType": "contract IERC20", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "totalShares",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "treasury",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "unpause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "userInfo",
        "outputs": [
            {"internalType": "uint256", "name": "shares", "type": "uint256"},
            {"internalType": "uint256", "name": "lastDepositedTime", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "cakeAtLastUserAction",
                "type": "uint256",
            },
            {
                "internalType": "uint256",
                "name": "lastUserActionTime",
                "type": "uint256",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_shares", "type": "uint256"}],
        "name": "withdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "withdrawAll",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "withdrawFee",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "withdrawFeePeriod",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
]

ZAPPER_EXCHANGE = [
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "quoteSigner",
                "type": "address",
            }
        ],
        "name": "QuoteSignerUpdated",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "taker",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "inputToken",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "outputToken",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "inputTokenAmount",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "outputTokenAmount",
                "type": "uint256",
            },
        ],
        "name": "TransformedERC20",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "transformerDeployer",
                "type": "address",
            }
        ],
        "name": "TransformerDeployerUpdated",
        "type": "event",
    },
    {
        "inputs": [],
        "name": "FEATURE_NAME",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "FEATURE_VERSION",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "address payable",
                        "name": "taker",
                        "type": "address",
                    },
                    {
                        "internalType": "contract IERC20TokenV06",
                        "name": "inputToken",
                        "type": "address",
                    },
                    {
                        "internalType": "contract IERC20TokenV06",
                        "name": "outputToken",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "inputTokenAmount",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "minOutputTokenAmount",
                        "type": "uint256",
                    },
                    {
                        "components": [
                            {
                                "internalType": "uint32",
                                "name": "deploymentNonce",
                                "type": "uint32",
                            },
                            {"internalType": "bytes", "name": "data", "type": "bytes"},
                        ],
                        "internalType": "struct ITransformERC20Feature.Transformation[]",
                        "name": "transformations",
                        "type": "tuple[]",
                    },
                    {"internalType": "bool", "name": "useSelfBalance", "type": "bool"},
                    {
                        "internalType": "address payable",
                        "name": "recipient",
                        "type": "address",
                    },
                ],
                "internalType": "struct ITransformERC20Feature.TransformERC20Args",
                "name": "args",
                "type": "tuple",
            }
        ],
        "name": "_transformERC20",
        "outputs": [
            {"internalType": "uint256", "name": "outputTokenAmount", "type": "uint256"}
        ],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "createTransformWallet",
        "outputs": [
            {
                "internalType": "contract IFlashWallet",
                "name": "wallet",
                "type": "address",
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getQuoteSigner",
        "outputs": [{"internalType": "address", "name": "signer", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getTransformWallet",
        "outputs": [
            {
                "internalType": "contract IFlashWallet",
                "name": "wallet",
                "type": "address",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getTransformerDeployer",
        "outputs": [{"internalType": "address", "name": "deployer", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "transformerDeployer",
                "type": "address",
            }
        ],
        "name": "migrate",
        "outputs": [{"internalType": "bytes4", "name": "success", "type": "bytes4"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "quoteSigner", "type": "address"}
        ],
        "name": "setQuoteSigner",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "transformerDeployer",
                "type": "address",
            }
        ],
        "name": "setTransformerDeployer",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract IERC20TokenV06",
                "name": "inputToken",
                "type": "address",
            },
            {
                "internalType": "contract IERC20TokenV06",
                "name": "outputToken",
                "type": "address",
            },
            {"internalType": "uint256", "name": "inputTokenAmount", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "minOutputTokenAmount",
                "type": "uint256",
            },
            {
                "components": [
                    {
                        "internalType": "uint32",
                        "name": "deploymentNonce",
                        "type": "uint32",
                    },
                    {"internalType": "bytes", "name": "data", "type": "bytes"},
                ],
                "internalType": "struct ITransformERC20Feature.Transformation[]",
                "name": "transformations",
                "type": "tuple[]",
            },
        ],
        "name": "transformERC20",
        "outputs": [
            {"internalType": "uint256", "name": "outputTokenAmount", "type": "uint256"}
        ],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract IERC20TokenV06",
                "name": "inputToken",
                "type": "address",
            },
            {
                "internalType": "contract IERC20TokenV06",
                "name": "outputToken",
                "type": "address",
            },
            {"internalType": "uint256", "name": "inputTokenAmount", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "minOutputTokenAmount",
                "type": "uint256",
            },
            {
                "components": [
                    {
                        "internalType": "uint32",
                        "name": "deploymentNonce",
                        "type": "uint32",
                    },
                    {"internalType": "bytes", "name": "data", "type": "bytes"},
                ],
                "internalType": "struct ITransformERC20Feature.Transformation[]",
                "name": "transformations",
                "type": "tuple[]",
            },
        ],
        "name": "transformERC20Staging",
        "outputs": [
            {"internalType": "uint256", "name": "outputTokenAmount", "type": "uint256"}
        ],
        "stateMutability": "payable",
        "type": "function",
    },
]

IFO_POOL = [
    {
        "inputs": [
            {"internalType": "contract IERC20", "name": "_token", "type": "address"},
            {
                "internalType": "contract IERC20",
                "name": "_receiptToken",
                "type": "address",
            },
            {
                "internalType": "contract IMasterChef",
                "name": "_masterchef",
                "type": "address",
            },
            {"internalType": "address", "name": "_admin", "type": "address"},
            {"internalType": "address", "name": "_treasury", "type": "address"},
            {"internalType": "uint256", "name": "_startBlock", "type": "uint256"},
            {"internalType": "uint256", "name": "_endBlock", "type": "uint256"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "shares",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "lastDepositedTime",
                "type": "uint256",
            },
        ],
        "name": "Deposit",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "performanceFee",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "callFee",
                "type": "uint256",
            },
        ],
        "name": "Harvest",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {"anonymous": false, "inputs": [], "name": "Pause", "type": "event"},
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "account",
                "type": "address",
            }
        ],
        "name": "Paused",
        "type": "event",
    },
    {"anonymous": false, "inputs": [], "name": "Unpause", "type": "event"},
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "account",
                "type": "address",
            }
        ],
        "name": "Unpaused",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "endBlock",
                "type": "uint256",
            }
        ],
        "name": "UpdateEndBlock",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "startBlock",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "endBlock",
                "type": "uint256",
            },
        ],
        "name": "UpdateStartAndEndBlocks",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "lastAvgBalance",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "lastActionBalance",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "lastValidActionBalance",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "lastActionBlock",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "lastValidActionBlock",
                "type": "uint256",
            },
        ],
        "name": "UpdateUserIFO",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "shares",
                "type": "uint256",
            },
        ],
        "name": "Withdraw",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "currentBlock",
                "type": "uint256",
            },
        ],
        "name": "ZeroFreeIFO",
        "type": "event",
    },
    {
        "inputs": [],
        "name": "MAX_CALL_FEE",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "MAX_PERFORMANCE_FEE",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "MAX_WITHDRAW_FEE",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "MAX_WITHDRAW_FEE_PERIOD",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "admin",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "available",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "calculateHarvestCakeRewards",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "calculateTotalPendingCakeRewards",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "callFee",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_amount", "type": "uint256"}],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "emergencyWithdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "emergencyWithdrawAll",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "endBlock",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getPricePerFullShare",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_user", "type": "address"}],
        "name": "getUserCredit",
        "outputs": [
            {"internalType": "uint256", "name": "avgBalance", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "harvest",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_token", "type": "address"}],
        "name": "inCaseTokensGetStuck",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "lastHarvestedTime",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "masterchef",
        "outputs": [
            {"internalType": "contract IMasterChef", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "pause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "paused",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "performanceFee",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "receiptToken",
        "outputs": [{"internalType": "contract IERC20", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_admin", "type": "address"}],
        "name": "setAdmin",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_callFee", "type": "uint256"}],
        "name": "setCallFee",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_performanceFee", "type": "uint256"}
        ],
        "name": "setPerformanceFee",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_treasury", "type": "address"}],
        "name": "setTreasury",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_withdrawFee", "type": "uint256"}
        ],
        "name": "setWithdrawFee",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_withdrawFeePeriod", "type": "uint256"}
        ],
        "name": "setWithdrawFeePeriod",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "startBlock",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "token",
        "outputs": [{"internalType": "contract IERC20", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "totalShares",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "treasury",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "unpause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_endBlock", "type": "uint256"}],
        "name": "updateEndBlock",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_startBlock", "type": "uint256"},
            {"internalType": "uint256", "name": "_endBlock", "type": "uint256"},
        ],
        "name": "updateStartAndEndBlocks",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "userIFOInfo",
        "outputs": [
            {"internalType": "uint256", "name": "lastActionBalance", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "lastValidActionBalance",
                "type": "uint256",
            },
            {"internalType": "uint256", "name": "lastActionBlock", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "lastValidActionBlock",
                "type": "uint256",
            },
            {"internalType": "uint256", "name": "lastAvgBalance", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "userInfo",
        "outputs": [
            {"internalType": "uint256", "name": "shares", "type": "uint256"},
            {"internalType": "uint256", "name": "lastDepositedTime", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "cakeAtLastUserAction",
                "type": "uint256",
            },
            {
                "internalType": "uint256",
                "name": "lastUserActionTime",
                "type": "uint256",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_shares", "type": "uint256"}],
        "name": "withdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "withdrawAll",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "withdrawFee",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "withdrawFeePeriod",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
]

PANCAKE_ROUTER_V2 = [
    {
        "inputs": [
            {"internalType": "address", "name": "_factory", "type": "address"},
            {"internalType": "address", "name": "_WETH", "type": "address"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "inputs": [],
        "name": "WETH",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "tokenA", "type": "address"},
            {"internalType": "address", "name": "tokenB", "type": "address"},
            {"internalType": "uint256", "name": "amountADesired", "type": "uint256"},
            {"internalType": "uint256", "name": "amountBDesired", "type": "uint256"},
            {"internalType": "uint256", "name": "amountAMin", "type": "uint256"},
            {"internalType": "uint256", "name": "amountBMin", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
        ],
        "name": "addLiquidity",
        "outputs": [
            {"internalType": "uint256", "name": "amountA", "type": "uint256"},
            {"internalType": "uint256", "name": "amountB", "type": "uint256"},
            {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "token", "type": "address"},
            {
                "internalType": "uint256",
                "name": "amountTokenDesired",
                "type": "uint256",
            },
            {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
            {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
        ],
        "name": "addLiquidityETH",
        "outputs": [
            {"internalType": "uint256", "name": "amountToken", "type": "uint256"},
            {"internalType": "uint256", "name": "amountETH", "type": "uint256"},
            {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
        ],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "factory",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
            {"internalType": "uint256", "name": "reserveIn", "type": "uint256"},
            {"internalType": "uint256", "name": "reserveOut", "type": "uint256"},
        ],
        "name": "getAmountIn",
        "outputs": [{"internalType": "uint256", "name": "amountIn", "type": "uint256"}],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "uint256", "name": "reserveIn", "type": "uint256"},
            {"internalType": "uint256", "name": "reserveOut", "type": "uint256"},
        ],
        "name": "getAmountOut",
        "outputs": [
            {"internalType": "uint256", "name": "amountOut", "type": "uint256"}
        ],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
        ],
        "name": "getAmountsIn",
        "outputs": [
            {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
        ],
        "name": "getAmountsOut",
        "outputs": [
            {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountA", "type": "uint256"},
            {"internalType": "uint256", "name": "reserveA", "type": "uint256"},
            {"internalType": "uint256", "name": "reserveB", "type": "uint256"},
        ],
        "name": "quote",
        "outputs": [{"internalType": "uint256", "name": "amountB", "type": "uint256"}],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "tokenA", "type": "address"},
            {"internalType": "address", "name": "tokenB", "type": "address"},
            {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
            {"internalType": "uint256", "name": "amountAMin", "type": "uint256"},
            {"internalType": "uint256", "name": "amountBMin", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
        ],
        "name": "removeLiquidity",
        "outputs": [
            {"internalType": "uint256", "name": "amountA", "type": "uint256"},
            {"internalType": "uint256", "name": "amountB", "type": "uint256"},
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "token", "type": "address"},
            {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
            {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
            {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
        ],
        "name": "removeLiquidityETH",
        "outputs": [
            {"internalType": "uint256", "name": "amountToken", "type": "uint256"},
            {"internalType": "uint256", "name": "amountETH", "type": "uint256"},
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "token", "type": "address"},
            {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
            {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
            {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
        ],
        "name": "removeLiquidityETHSupportingFeeOnTransferTokens",
        "outputs": [
            {"internalType": "uint256", "name": "amountETH", "type": "uint256"}
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "token", "type": "address"},
            {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
            {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
            {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            {"internalType": "bool", "name": "approveMax", "type": "bool"},
            {"internalType": "uint8", "name": "v", "type": "uint8"},
            {"internalType": "bytes32", "name": "r", "type": "bytes32"},
            {"internalType": "bytes32", "name": "s", "type": "bytes32"},
        ],
        "name": "removeLiquidityETHWithPermit",
        "outputs": [
            {"internalType": "uint256", "name": "amountToken", "type": "uint256"},
            {"internalType": "uint256", "name": "amountETH", "type": "uint256"},
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "token", "type": "address"},
            {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
            {"internalType": "uint256", "name": "amountTokenMin", "type": "uint256"},
            {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            {"internalType": "bool", "name": "approveMax", "type": "bool"},
            {"internalType": "uint8", "name": "v", "type": "uint8"},
            {"internalType": "bytes32", "name": "r", "type": "bytes32"},
            {"internalType": "bytes32", "name": "s", "type": "bytes32"},
        ],
        "name": "removeLiquidityETHWithPermitSupportingFeeOnTransferTokens",
        "outputs": [
            {"internalType": "uint256", "name": "amountETH", "type": "uint256"}
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "tokenA", "type": "address"},
            {"internalType": "address", "name": "tokenB", "type": "address"},
            {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
            {"internalType": "uint256", "name": "amountAMin", "type": "uint256"},
            {"internalType": "uint256", "name": "amountBMin", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            {"internalType": "bool", "name": "approveMax", "type": "bool"},
            {"internalType": "uint8", "name": "v", "type": "uint8"},
            {"internalType": "bytes32", "name": "r", "type": "bytes32"},
            {"internalType": "bytes32", "name": "s", "type": "bytes32"},
        ],
        "name": "removeLiquidityWithPermit",
        "outputs": [
            {"internalType": "uint256", "name": "amountA", "type": "uint256"},
            {"internalType": "uint256", "name": "amountB", "type": "uint256"},
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
        ],
        "name": "swapETHForExactTokens",
        "outputs": [
            {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
        ],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
        ],
        "name": "swapExactETHForTokens",
        "outputs": [
            {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
        ],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
        ],
        "name": "swapExactETHForTokensSupportingFeeOnTransferTokens",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
        ],
        "name": "swapExactTokensForETH",
        "outputs": [
            {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
        ],
        "name": "swapExactTokensForETHSupportingFeeOnTransferTokens",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
        ],
        "name": "swapExactTokensForTokens",
        "outputs": [
            {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
        ],
        "name": "swapExactTokensForTokensSupportingFeeOnTransferTokens",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
            {"internalType": "uint256", "name": "amountInMax", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
        ],
        "name": "swapTokensForExactETH",
        "outputs": [
            {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
            {"internalType": "uint256", "name": "amountInMax", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "deadline", "type": "uint256"},
        ],
        "name": "swapTokensForExactTokens",
        "outputs": [
            {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {"stateMutability": "payable", "type": "receive"},
]

AAVE_ZAP_IN = [
    {
        "inputs": [
            {"internalType": "address[]", "name": "targets", "type": "address[]"},
            {"internalType": "uint256", "name": "_goodwill", "type": "uint256"},
            {"internalType": "uint256", "name": "_affiliateSplit", "type": "uint256"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "sender",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "token",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "tokensRec",
                "type": "uint256",
            },
        ],
        "name": "zapIn",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "sender",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "token",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "tokensRec",
                "type": "uint256",
            },
        ],
        "name": "zapOut",
        "type": "event",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "fromToken", "type": "address"},
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "address", "name": "aToken", "type": "address"},
            {"internalType": "uint256", "name": "minATokens", "type": "uint256"},
            {"internalType": "address", "name": "swapTarget", "type": "address"},
            {"internalType": "bytes", "name": "swapData", "type": "bytes"},
            {"internalType": "address", "name": "affiliate", "type": "address"},
        ],
        "name": "ZapIn",
        "outputs": [
            {"internalType": "uint256", "name": "aTokensRec", "type": "uint256"}
        ],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "fromToken", "type": "address"},
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "address", "name": "toToken", "type": "address"},
            {"internalType": "uint256", "name": "minToTokens", "type": "uint256"},
            {"internalType": "address", "name": "swapTarget", "type": "address"},
            {"internalType": "bytes", "name": "swapData", "type": "bytes"},
            {"internalType": "address", "name": "affiliate", "type": "address"},
        ],
        "name": "ZapOut",
        "outputs": [
            {"internalType": "uint256", "name": "tokensRec", "type": "uint256"}
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "fromToken", "type": "address"},
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "address", "name": "toToken", "type": "address"},
            {"internalType": "uint256", "name": "minToTokens", "type": "uint256"},
            {"internalType": "bytes", "name": "permitSig", "type": "bytes"},
            {"internalType": "address", "name": "swapTarget", "type": "address"},
            {"internalType": "bytes", "name": "swapData", "type": "bytes"},
            {"internalType": "address", "name": "affiliate", "type": "address"},
        ],
        "name": "ZapOutWithPermit",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"},
        ],
        "name": "affiliateBalance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "affiliates",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address[]", "name": "tokens", "type": "address[]"}
        ],
        "name": "affilliateWithdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "approvedTargets",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "feeWhitelist",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "aToken", "type": "address"}],
        "name": "getUnderlyingToken",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "goodwill",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address[]", "name": "targets", "type": "address[]"},
            {"internalType": "bool[]", "name": "isApproved", "type": "bool[]"},
        ],
        "name": "setApprovedTargets",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_affiliate", "type": "address"},
            {"internalType": "bool", "name": "_status", "type": "bool"},
        ],
        "name": "set_affiliate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "zapAddress", "type": "address"},
            {"internalType": "bool", "name": "status", "type": "bool"},
        ],
        "name": "set_feeWhitelist",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_new_affiliateSplit",
                "type": "uint256",
            }
        ],
        "name": "set_new_affiliateSplit",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_new_goodwill", "type": "uint256"}
        ],
        "name": "set_new_goodwill",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "stopped",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "toggleContractActive",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "totalAffiliateBalance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address[]", "name": "tokens", "type": "address[]"}
        ],
        "name": "withdrawTokens",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {"stateMutability": "payable", "type": "receive"},
]

ZAPPER_LP = [
    {
        "inputs": [
            {"internalType": "uint256", "name": "_goodwill", "type": "uint256"},
            {"internalType": "uint256", "name": "_affiliateSplit", "type": "uint256"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "sender",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "pool",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "tokensRec",
                "type": "uint256",
            },
        ],
        "name": "zapIn",
        "type": "event",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_FromTokenContractAddress",
                "type": "address",
            },
            {"internalType": "address", "name": "_pairAddress", "type": "address"},
            {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            {"internalType": "uint256", "name": "_minPoolTokens", "type": "uint256"},
            {"internalType": "address", "name": "_swapTarget", "type": "address"},
            {"internalType": "bytes", "name": "swapData", "type": "bytes"},
            {"internalType": "address", "name": "affiliate", "type": "address"},
            {"internalType": "bool", "name": "transferResidual", "type": "bool"},
            {"internalType": "bool", "name": "shouldSellEntireBalance", "type": "bool"},
        ],
        "name": "ZapIn",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"},
        ],
        "name": "affiliateBalance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "affiliates",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address[]", "name": "tokens", "type": "address[]"}
        ],
        "name": "affilliateWithdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "approvedTargets",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "feeWhitelist",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "goodwill",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address[]", "name": "targets", "type": "address[]"},
            {"internalType": "bool[]", "name": "isApproved", "type": "bool[]"},
        ],
        "name": "setApprovedTargets",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_affiliate", "type": "address"},
            {"internalType": "bool", "name": "_status", "type": "bool"},
        ],
        "name": "set_affiliate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "zapAddress", "type": "address"},
            {"internalType": "bool", "name": "status", "type": "bool"},
        ],
        "name": "set_feeWhitelist",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_new_affiliateSplit",
                "type": "uint256",
            }
        ],
        "name": "set_new_affiliateSplit",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_new_goodwill", "type": "uint256"}
        ],
        "name": "set_new_goodwill",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "stopped",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "toggleContractActive",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "totalAffiliateBalance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address[]", "name": "tokens", "type": "address[]"}
        ],
        "name": "withdrawTokens",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {"stateMutability": "payable", "type": "receive"},
]

ZAPPER_NFT = [
    {
        "inputs": [
            {"internalType": "string", "name": "_name", "type": "string"},
            {"internalType": "string", "name": "_symbol", "type": "string"},
            {"internalType": "string", "name": "_uri", "type": "string"},
            {"internalType": "address", "name": "signer", "type": "address"},
            {"internalType": "address", "name": "manager", "type": "address"},
            {"internalType": "uint256", "name": "_deadline", "type": "uint256"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "id",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "cost",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "nextRarity",
                "type": "uint256",
            },
        ],
        "name": "Add",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "account",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "operator",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "bool",
                "name": "approved",
                "type": "bool",
            },
        ],
        "name": "ApprovalForAll",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "account",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "voltsBurned",
                "type": "uint256",
            },
        ],
        "name": "BurnVolts",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "account",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "voltsRecieved",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "nonce",
                "type": "uint256",
            },
        ],
        "name": "ClaimVolts",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "account",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "craftID",
                "type": "uint256",
            },
        ],
        "name": "Craft",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "account",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256[]",
                "name": "craftIDs",
                "type": "uint256[]",
            },
        ],
        "name": "CraftBatch",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "account",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "voltsSpent",
                "type": "uint256",
            },
        ],
        "name": "Mint",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "account",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "voltsRecieved",
                "type": "uint256",
            },
        ],
        "name": "Redeem",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "operator",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "from",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "to",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256[]",
                "name": "ids",
                "type": "uint256[]",
            },
            {
                "indexed": false,
                "internalType": "uint256[]",
                "name": "values",
                "type": "uint256[]",
            },
        ],
        "name": "TransferBatch",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "operator",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "from",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "to",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "id",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
            },
        ],
        "name": "TransferSingle",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "string",
                "name": "value",
                "type": "string",
            },
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "id",
                "type": "uint256",
            },
        ],
        "name": "URI",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "string",
                "name": "uri",
                "type": "string",
            }
        ],
        "name": "updateBaseURI",
        "type": "event",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "accessoryContract",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256[]", "name": "ids", "type": "uint256[]"},
            {"internalType": "uint256[]", "name": "costs", "type": "uint256[]"},
            {"internalType": "uint256[]", "name": "nextRarities", "type": "uint256[]"},
        ],
        "name": "add",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "uint256", "name": "id", "type": "uint256"},
        ],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address[]", "name": "accounts", "type": "address[]"},
            {"internalType": "uint256[]", "name": "ids", "type": "uint256[]"},
        ],
        "name": "balanceOfBatch",
        "outputs": [{"internalType": "uint256[]", "name": "", "type": "uint256[]"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "id", "type": "uint256"},
            {"internalType": "uint256", "name": "quantity", "type": "uint256"},
        ],
        "name": "burn",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256[]", "name": "ids", "type": "uint256[]"},
            {"internalType": "uint256[]", "name": "quantities", "type": "uint256[]"},
        ],
        "name": "burnBatch",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "voltsBurned", "type": "uint256"}
        ],
        "name": "burnVolts",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "voltsEarned", "type": "uint256"},
            {"internalType": "bytes", "name": "signature", "type": "bytes"},
        ],
        "name": "claimVolts",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "name": "cost",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "id", "type": "uint256"},
            {"internalType": "uint256", "name": "quantity", "type": "uint256"},
        ],
        "name": "craft",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256[]", "name": "ids", "type": "uint256[]"},
            {"internalType": "uint256[]", "name": "quantities", "type": "uint256[]"},
        ],
        "name": "craftBatch",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "craftingRequirement",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "deadline",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "uint256", "name": "volts", "type": "uint256"},
            {"internalType": "uint256", "name": "nonce", "type": "uint256"},
        ],
        "name": "getMessageHash",
        "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "address", "name": "operator", "type": "address"},
        ],
        "name": "isApprovedForAll",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "id", "type": "uint256"},
            {"internalType": "uint256", "name": "quantity", "type": "uint256"},
        ],
        "name": "mint",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256[]", "name": "ids", "type": "uint256[]"},
            {"internalType": "uint256[]", "name": "quantities", "type": "uint256[]"},
        ],
        "name": "mintBatch",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "name": "nextRarity",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "nonces",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "pause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "paused",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "id", "type": "uint256"},
            {"internalType": "uint256", "name": "quantity", "type": "uint256"},
        ],
        "name": "redeem",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256[]", "name": "ids", "type": "uint256[]"},
            {"internalType": "uint256[]", "name": "quantities", "type": "uint256[]"},
        ],
        "name": "redeemBatch",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "redeemModifier",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "from", "type": "address"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256[]", "name": "ids", "type": "uint256[]"},
            {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"},
            {"internalType": "bytes", "name": "data", "type": "bytes"},
        ],
        "name": "safeBatchTransferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "from", "type": "address"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "id", "type": "uint256"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "bytes", "name": "data", "type": "bytes"},
        ],
        "name": "safeTransferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "operator", "type": "address"},
            {"internalType": "bool", "name": "approved", "type": "bool"},
        ],
        "name": "setApprovalForAll",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "string", "name": "_uri", "type": "string"}],
        "name": "setBaseURI",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "signer",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "bytes4", "name": "interfaceId", "type": "bytes4"}],
        "name": "supportsInterface",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "id", "type": "uint256"}],
        "name": "totalSupply",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_accessoryContract",
                "type": "address",
            },
            {"internalType": "bool", "name": "allowed", "type": "bool"},
        ],
        "name": "updateAccessoryContracts",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256[]", "name": "ids", "type": "uint256[]"},
            {"internalType": "uint256[]", "name": "costs", "type": "uint256[]"},
            {"internalType": "uint256[]", "name": "nextRarities", "type": "uint256[]"},
        ],
        "name": "updateCraftingParameters",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_craftingRequirement",
                "type": "uint256",
            }
        ],
        "name": "updateCraftingRequirement",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_deadline", "type": "uint256"}],
        "name": "updateDeadline",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_redeemModifier", "type": "uint256"}
        ],
        "name": "updateRedeemModifier",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "id", "type": "uint256"}],
        "name": "uri",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "voltBalance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "voltSupply",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
]
ZERO_X = [
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "quoteSigner",
                "type": "address",
            }
        ],
        "name": "QuoteSignerUpdated",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "taker",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "inputToken",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "outputToken",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "inputTokenAmount",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "outputTokenAmount",
                "type": "uint256",
            },
        ],
        "name": "TransformedERC20",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "transformerDeployer",
                "type": "address",
            }
        ],
        "name": "TransformerDeployerUpdated",
        "type": "event",
    },
    {
        "inputs": [],
        "name": "FEATURE_NAME",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "FEATURE_VERSION",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "address payable",
                        "name": "taker",
                        "type": "address",
                    },
                    {
                        "internalType": "contract IERC20TokenV06",
                        "name": "inputToken",
                        "type": "address",
                    },
                    {
                        "internalType": "contract IERC20TokenV06",
                        "name": "outputToken",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "inputTokenAmount",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "minOutputTokenAmount",
                        "type": "uint256",
                    },
                    {
                        "components": [
                            {
                                "internalType": "uint32",
                                "name": "deploymentNonce",
                                "type": "uint32",
                            },
                            {"internalType": "bytes", "name": "data", "type": "bytes"},
                        ],
                        "internalType": "struct ITransformERC20Feature.Transformation[]",
                        "name": "transformations",
                        "type": "tuple[]",
                    },
                    {"internalType": "bool", "name": "useSelfBalance", "type": "bool"},
                    {
                        "internalType": "address payable",
                        "name": "recipient",
                        "type": "address",
                    },
                ],
                "internalType": "struct ITransformERC20Feature.TransformERC20Args",
                "name": "args",
                "type": "tuple",
            }
        ],
        "name": "_transformERC20",
        "outputs": [
            {"internalType": "uint256", "name": "outputTokenAmount", "type": "uint256"}
        ],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "createTransformWallet",
        "outputs": [
            {
                "internalType": "contract IFlashWallet",
                "name": "wallet",
                "type": "address",
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getQuoteSigner",
        "outputs": [{"internalType": "address", "name": "signer", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getTransformWallet",
        "outputs": [
            {
                "internalType": "contract IFlashWallet",
                "name": "wallet",
                "type": "address",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getTransformerDeployer",
        "outputs": [{"internalType": "address", "name": "deployer", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "transformerDeployer",
                "type": "address",
            }
        ],
        "name": "migrate",
        "outputs": [{"internalType": "bytes4", "name": "success", "type": "bytes4"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "quoteSigner", "type": "address"}
        ],
        "name": "setQuoteSigner",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "transformerDeployer",
                "type": "address",
            }
        ],
        "name": "setTransformerDeployer",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract IERC20TokenV06",
                "name": "inputToken",
                "type": "address",
            },
            {
                "internalType": "contract IERC20TokenV06",
                "name": "outputToken",
                "type": "address",
            },
            {"internalType": "uint256", "name": "inputTokenAmount", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "minOutputTokenAmount",
                "type": "uint256",
            },
            {
                "components": [
                    {
                        "internalType": "uint32",
                        "name": "deploymentNonce",
                        "type": "uint32",
                    },
                    {"internalType": "bytes", "name": "data", "type": "bytes"},
                ],
                "internalType": "struct ITransformERC20Feature.Transformation[]",
                "name": "transformations",
                "type": "tuple[]",
            },
        ],
        "name": "transformERC20",
        "outputs": [
            {"internalType": "uint256", "name": "outputTokenAmount", "type": "uint256"}
        ],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract IERC20TokenV06",
                "name": "inputToken",
                "type": "address",
            },
            {
                "internalType": "contract IERC20TokenV06",
                "name": "outputToken",
                "type": "address",
            },
            {"internalType": "uint256", "name": "inputTokenAmount", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "minOutputTokenAmount",
                "type": "uint256",
            },
            {
                "components": [
                    {
                        "internalType": "uint32",
                        "name": "deploymentNonce",
                        "type": "uint32",
                    },
                    {"internalType": "bytes", "name": "data", "type": "bytes"},
                ],
                "internalType": "struct ITransformERC20Feature.Transformation[]",
                "name": "transformations",
                "type": "tuple[]",
            },
        ],
        "name": "transformERC20Staging",
        "outputs": [
            {"internalType": "uint256", "name": "outputTokenAmount", "type": "uint256"}
        ],
        "stateMutability": "payable",
        "type": "function",
    },
]

USDT = [
    {
        "inputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "owner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "spender",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
            },
        ],
        "name": "Approval",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "from",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "to",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
            },
        ],
        "name": "Transfer",
        "type": "event",
    },
    {
        "constant": true,
        "inputs": [],
        "name": "_decimals",
        "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": true,
        "inputs": [],
        "name": "_name",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": true,
        "inputs": [],
        "name": "_symbol",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": true,
        "inputs": [
            {"internalType": "address", "name": "owner", "type": "address"},
            {"internalType": "address", "name": "spender", "type": "address"},
        ],
        "name": "allowance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": false,
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "approve",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": true,
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": false,
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "burn",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": true,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": false,
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "subtractedValue", "type": "uint256"},
        ],
        "name": "decreaseAllowance",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": true,
        "inputs": [],
        "name": "getOwner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": false,
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "addedValue", "type": "uint256"},
        ],
        "name": "increaseAllowance",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": false,
        "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
        "name": "mint",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": true,
        "inputs": [],
        "name": "name",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": true,
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": false,
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": true,
        "inputs": [],
        "name": "symbol",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": false,
        "inputs": [
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": false,
        "inputs": [
            {"internalType": "address", "name": "sender", "type": "address"},
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "transferFrom",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": false,
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function",
    },
]
