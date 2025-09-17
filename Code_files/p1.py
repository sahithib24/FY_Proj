#Day 16 Implement fog nodes with limited resources.

import random
import time

# ----------------------------
# Fog Node Class
# ----------------------------
class FogNode:
    def __init__(self, node_id, cpu_capacity, mem_capacity, storage_capacity):
        self.node_id = node_id
        self.total_cpu = cpu_capacity
        self.total_mem = mem_capacity
        self.total_storage = storage_capacity

        # Track available resources
        self.available_cpu = cpu_capacity
        self.available_mem = mem_capacity
        self.available_storage = storage_capacity

    def can_allocate(self, req):
        """Check if this node can serve the request."""
        return (req["CPU"] <= self.available_cpu and
                req["Memory"] <= self.available_mem and
                req["Storage"] <= self.available_storage)

    def allocate(self, req):
        """Allocate resources if possible."""
        if self.can_allocate(req):
            self.available_cpu -= req["CPU"]
            self.available_mem -= req["Memory"]
            self.available_storage -= req["Storage"]
            print(f"✅ Request {req['UserID']} allocated to Node {self.node_id}")
            return True
        else:
            print(f"❌ Request {req['UserID']} rejected by Node {self.node_id} (Not enough resources)")
            return False

    def __str__(self):
        return (f"FogNode {self.node_id} | "
                f"CPU {self.available_cpu}/{self.total_cpu}, "
                f"Memory {self.available_mem}/{self.total_mem}, "
                f"Storage {self.available_storage}/{self.total_storage}")

# ----------------------------
# Generate Random User Request (Day 15)
# ----------------------------
def generate_user_request(user_id):
    cpu = random.randint(1, 8)
    memory = random.choice([2, 4, 8, 16])
    storage = random.choice([50, 100, 200])
    deadline = random.choice([5, 10, 20, 30])
    return {
        "UserID": user_id,
        "CPU": cpu,
        "Memory": memory,
        "Storage": storage,
        "Deadline": deadline,
        "RequestTime": int(time.time())
    }

# ----------------------------
# Simulation
# ----------------------------
if __name__ == "__main__":
    # Step 1: Create Fog Nodes
    fog_nodes = [
        FogNode(1, cpu_capacity=16, mem_capacity=64, storage_capacity=500),
        FogNode(2, cpu_capacity=8, mem_capacity=32, storage_capacity=300)
    ]

    # Step 2: Generate Requests
    requests = [generate_user_request(i) for i in range(1, 11)]

    # Step 3: Try to allocate requests
    for req in requests:
        allocated = False
        for node in fog_nodes:
            if node.allocate(req):
                allocated = True
                break
        if not allocated:
            print(f"⚠️ Request {req['UserID']} could not be served by any node")

    # Step 4: Print final status
    print("\n--- Final Fog Node Status ---")
    for node in fog_nodes:
        print(node)

# Fog nodes have limited resources.

# Each incoming request is checked before allocation.

# If resources are available → allocate.

# If not → request is rejected or forwarded.


#Day 17 Random Assignment

# import random

# # Example users (from Day 15)
# users = [
#     {"id": 1, "cpu": 2, "memory": 4, "latency": 10},
#     {"id": 2, "cpu": 1, "memory": 2, "latency": 20},
#     {"id": 3, "cpu": 3, "memory": 6, "latency": 15}
# ]

# # Example fog nodes (from Day 16)
# fog_nodes = [
#     {"id": "Fog1", "cpu": 10, "memory": 20},
#     {"id": "Fog2", "cpu": 8, "memory": 15},
#     {"id": "Fog3", "cpu": 12, "memory": 25}
# ]

# # Random assignment (baseline)
# assignments = {}
# for user in users:
#     node = random.choice(fog_nodes)  # pick any fog node
#     assignments[user["id"]] = node["id"]

# print("Baseline Assignments:", assignments)
