# 2252 줄 세우기
from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int, input().strip().split())
graph = {i:[] for i in range(1, N+1)}
in_degree = [0] * (N+1)
result = []

for _ in range(M):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    in_degree[b] += 1

def topology_sort():
    queue = deque()
    for v in range(N):
        if in_degree[v] == 0:
            queue.append(v)
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for i in graph[node]:
            in_degree[i] -= 1
            if in_degree == 0:
                queue.append(i)




















def topology_sort():        
    queue = deque()
    for v in range(1, N+1):
        if in_degree[v] == 0:
            queue.append(v)
    
    while queue:
        v = queue.popleft()
        result.append(v)

        for i in graph[v]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)

topology_sort()

for i in result:
    print(i, end=' ')
