# Sample adjacency list using a dictionary
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

# Print the adjacency list
for node, neighbors in graph.items():
    print(f"{node}: {neighbors}")
    print("---------------------------")


# Sample adjacency list using a dictionary with numbers
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2, 6],
    6: [3, 5]
}

# Print the adjacency list
for node, neighbors in graph.items():
    print(f"{node}: {neighbors}")
