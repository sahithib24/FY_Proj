# Introduce a basic fixed pricing system so that every request assigned to a fog node has a predictable cost.
# This step adds the pricing dimension before we move to dynamic or adaptive pricing later.

# Steps

# Define Fixed Prices per Resource Unit:

# CPU = e.g., ₹2 per unit

# Memory = e.g., ₹1 per unit

# (Optional: add bandwidth/latency cost later)

# For each user request:

# Multiply resource usage by fixed price.

# Total cost = (CPU used × CPU price) + (Memory used × Memory price).

# Assign cost to request:

# After assigning the user to a fog node (from Day 17), calculate and attach the cost.

# At this stage:

# Every request has a deterministic cost.

# Easy to compare later with dynamic pricing models (GTRA, FogPrime, etc.).

import random

# Users (Day 15)
users = [
    {"id": 1, "cpu": 2, "memory": 4, "latency": 10},
    {"id": 2, "cpu": 1, "memory": 2, "latency": 20},
    {"id": 3, "cpu": 3, "memory": 6, "latency": 15}
]

# Fog nodes (Day 16)
fog_nodes = [
    {"id": "Fog1", "cpu": 10, "memory": 20},
    {"id": "Fog2", "cpu": 8, "memory": 15},
    {"id": "Fog3", "cpu": 12, "memory": 25}
]

# Fixed prices
PRICE_CPU = 2   # cost per unit of CPU
PRICE_MEM = 1   # cost per unit of Memory

assignments = {}
for user in users:
    node = random.choice(fog_nodes)  # baseline random assignment (Day 17)
    # Calculate fixed price
    cost = (user["cpu"] * PRICE_CPU) + (user["memory"] * PRICE_MEM)
    assignments[user["id"]] = {"fog_node": node["id"], "cost": cost}

print("Assignments with Fixed Pricing:", assignments)
