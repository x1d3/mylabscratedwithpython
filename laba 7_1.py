from math import inf
from collections import defaultdict

graph = {
    1: {2: 4, 3: 3},
    2: {1: 4, 4: 6, 6: 2},
    3: {1: 3, 5: 2, 6: 8},
    4: {2: 6, 6: 1, 7: 3},
    5: {3: 2, 6: 4, 7: 2},
    6: {2: 2, 3: 8, 4: 1, 5: 4},
    7: {4: 3, 5: 2}
}

path_len = defaultdict(lambda: inf)
visited = set()
node = 1
value = 0
final_node = 7

path_len[node] = value
while node != final_node and visited != set(graph.keys()):
    for next_node in (graph[node].keys() - visited):
        new_value = value + graph[node][next_node]
        if new_value < path_len[next_node]:
            path_len[next_node] = new_value
    visited.add(node)
    path_len[node] = inf
    node, value = max((node, value) for node, value in path_len.items() if node not in visited)

print(path_len[final_node])
