# 2606 바이러스

import sys
input = sys.stdin.readline

v_count = int(input().strip())
e_count = int(input().strip())
graph = {i:[] for i in range(1, v_count + 1)}
visited = [False] * (v_count + 1)
count = 0

def dfs(v):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)


for _ in range(e_count):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)
dfs(1)

print(sum(visited))
