#Day 19-21 Test the Fixed Pricing System and Visualize Results (Cost vs Demand)

import random
import matplotlib.pyplot as plt

# Prices
PRICE_CPU = 2
PRICE_MEM = 1

# Generate random user requests
def generate_requests(n=20):
    requests = []
    for i in range(n):
        requests.append({
            "id": i,
            "cpu": random.randint(1, 5),
            "memory": random.randint(1, 10)
        })
    return requests

# Calculate cost
def calculate_cost(request):
    return request["cpu"] * PRICE_CPU + request["memory"] * PRICE_MEM

# Test run
requests = generate_requests(20)
costs = [calculate_cost(r) for r in requests]
demands = [r["cpu"] + r["memory"] for r in requests]  # simple demand metric

# Sort by demand for smooth line
sorted_pairs = sorted(zip(demands, costs), key=lambda x: x[0])
sorted_demands, sorted_costs = zip(*sorted_pairs)

# Plot scatter + line
plt.scatter(sorted_demands, sorted_costs, color="blue", label="Requests")
plt.plot(sorted_demands, sorted_costs, color="red", linestyle="--", label="Cost Trend")
plt.xlabel("Total Demand (CPU + Memory)")
plt.ylabel("Cost (Fixed Pricing)")
plt.title("Cost vs Demand (Fixed Pricing Baseline)")
plt.legend()
plt.show()


# Baseline Observations

# Pricing Nature:

# Costs increase linearly with demand since the system uses a fixed per-unit price.

# Fairness:

# Every user pays proportionally to their resource usage.

# No consideration of fog node availability or congestion yet.

# Provider Perspective:

# Predictable but may be less profitable if demand is high (no surge pricing).

# User Perspective:

# Transparent, easy to understand.

# Good for trust, but not optimal for providers.