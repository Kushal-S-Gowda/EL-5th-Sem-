import random

def mobility_score(plan):
    density_penalty = plan["fsi"] / 5.0
    return max(0.4, 1.0 - density_penalty + random.uniform(-0.05, 0.05))
