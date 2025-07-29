import networkx as nx
import random
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add users (nodes)
users = ["Alice", "Bob", "Charlie", "Dina", "Elias"]
G.add_nodes_from(users)

# Randomly connect users (edges)
for user1 in users:
    for user2 in users:
        if user1 != user2 and random.random() > 0.5:
            G.add_edge(user1, user2)

# Print connections
print("Social Network Connections:")
for user in users:
    friends = list(G.neighbors(user))
    print(f"{user} is friends with {friends}")

# Optional: simulate message spreading
def spread_message(graph, sender, message):
    print(f"\n{sender} says: {message}")
    visited = set()
    queue = [sender]

    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.add(current)
            print(f"{current} received the message.")
            queue.extend(graph.neighbors(current))

spread_message(G, "Alice", "Hello everyone!")
# visualize the graph
nx.draw(G, with_labels=True)
plt.show()
