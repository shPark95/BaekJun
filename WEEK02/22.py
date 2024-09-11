# 11724 연결 요소의 개수

import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
N,M = map(int, input().split())
graph = {i:[] for i in range(1, N+1)}

def dfs(v, visited):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, visited)

def count_connected(v):
    count = 0
    visited = [False] * (N+1)
    for node in range(V):
        if not visited[node]:
            dfs(v, visited)
            count += 1
    return count

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


print(count_connected(N))










def dfs(graph, visited, node):
    visited[node] = True
    for node in graph[node]:
        if not visited[node]:
            dfs(graph, visited, node)

def count_connected(n, graph):
    visited = [False] * (n + 1)
    count = 0

    for node in range(1, n+1):
        if not visited[node]:
            dfs(graph, visited, node)
            count += 1

    return count

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


print(count_connected(N, graph))