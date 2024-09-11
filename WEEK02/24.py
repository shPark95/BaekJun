# 11725 트리의 부모 찾기
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input().strip())
graph = {i:[] for i in range(1, N+1)}
visited = [False] * (N+1)
parents = [0] * (N+1)

def dfs(node):
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            parents[neighbor] = node
            dfs(neighbor)

for _ in range(N-1):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

# Start DFS from node 1
visited[1] = True
dfs(1)

# Output results
result = '\n'.join(str(parents[i]) for i in range(2, N + 1))
print(result)

# from collections import deque, defaultdict

# def find_parents(n, edges):
#     graph = defaultdict(list)
#     for a, b in edges:
#         graph[a].append(b)
#         graph[b].append(a)
    
#     parents = [0] * (n + 1)
#     visited = [False] * (n + 1)
    
#     # BFS initialization
#     queue = deque([1])
#     visited[1] = True
#     while queue:
#         node = queue.popleft()
#         for neighbor in graph[node]:
#             if not visited[neighbor]:
#                 visited[neighbor] = True
#                 parents[neighbor] = node
#                 queue.append(neighbor)
    
#     # Output results
#     result = '\n'.join(str(parents[i]) for i in range(2, n + 1))
#     return result

# # Input example
# n = int(input())
# edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# print(find_parents(n, edges))