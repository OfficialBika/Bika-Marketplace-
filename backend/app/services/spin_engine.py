import random

REWARDS = [
    {"type": "coin", "amount": 10},
    {"type": "coin", "amount": 50},
    {"type": "coin", "amount": 100},
    {"type": "nft", "rarity": "Mystical"},
    {"type": "free_spin", "amount": 1},
]


def spin_wheel():
    return random.choice(REWARDS)
