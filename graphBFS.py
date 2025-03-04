from collections import deque

def bfs(adj, node):
    q = deque()
    visited = [False] * len(adj)
    visited[node] = True
    q.append(node)

    while q:
        curr = q.popleft()
        print("curr", curr)

        for i in adj[curr]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == '__main__':
    V = 5
    adj = [[] for _ in range(V)]
    print(adj)
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 2, 4)
    add_edge(adj, 3, 4)
    print(adj)
    bfs(adj, 0)
