from scripts.contract_abi import *
from brownie import Contract

zeroX = Contract.from_abi("0x", "0xdef1c0ded9bec7f1a1670819833240f027b25eff", ZERO_X)

ifo_pool_contract = Contract.from_abi(
    "IFO POOL", "0x1B2A2f6ed4A1401E8C73B4c2B6172455ce2f78E8", IFO_POOL
)

pancake_contract = Contract.from_abi(
    "Pancake", "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82", PANCAKE
)

pancake_router_v2 = Contract.from_abi(
    "Pancake Router V2", "0x10ED43C718714eb63d5aA57B78B54704E256024E", PANCAKE_ROUTER_V2
)

BSC_USDT_contract = Contract.from_abi(
    "USDT", "0x55d398326f99059fF775485246999027B3197955", USDT
)

ERA7_SYRUP = Contract.from_abi(
    "ERA7 SYRUP", "0x260F95f5b7FD8eda720ED9d0829164dE35B048ab", SYRUP_POOL
)

ERA7_token = Contract.from_abi(
    "ERA7", "0x6f9F0c4ad9Af7EbD61Ac5A1D4e0F2227F7B0E5f9", ERA7
)

ERA_IFO_contract = Contract.from_abi(
    "FROYO IFO", "0x527201a43f8da24ce9b7c21744a0706942f41fa3", IFO_3_1
)
