def dfsRecursive(adj, visited, node):
    visited[node] = True
    print("curr", node)

    for i in adj[node]:
        if not visited[i]:
            dfsRecursive(adj, visited, i)

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == '__main__':
    V = 5
    adj = [[] for _ in range(V)]
    print(adj)
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 0, 3)
    # add_edge(adj, 1, 2)
    add_edge(adj, 2, 3)
    add_edge(adj, 2, 4)
    # add_edge(adj, 3, 4)
    print(adj)
    visited = [False] * len(adj)
    dfsRecursive(adj, visited, 1)
