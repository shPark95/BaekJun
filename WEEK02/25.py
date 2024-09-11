# 1707 이분 그래프

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v, color):
    visited[v] = color
    for node in graph[v]:
        if visited[node] is None:
            if not dfs(node, not color):
                return False
        elif visited[node] == visited[v]:
            return False
    return True

K = int(input().strip())
for _ in range(K):
    V, E = map(int, input().strip().split())
    graph = {i: [] for i in range(1, V + 1)}
    visited = [None] * (V + 1)  # 방문 기록과 색상 (None이면 방문 안 함)
    
    for _ in range(E):
        u, v = map(int, input().strip().split())
        graph[u].append(v)
        graph[v].append(u)
    
    is_bipartite = True
    for i in range(1, V + 1):
        if visited[i] is None:
            if not dfs(i, True):
                is_bipartite = False
                break
    
    if is_bipartite:
        print("YES")
    else:
        print("NO")


# from collections import deque

# def is_bipartite(V, graph):
#     color = [-1] * (V + 1)
    
#     for start in range(1, V + 1):
#         if color[start] == -1:  # If the node hasn't been colored yet
#             queue = deque([start])
#             color[start] = 0  # Start coloring with color 0

#             while queue:
#                 node = queue.popleft()
#                 current_color = color[node]

#                 for neighbor in graph[node]:
#                     if color[neighbor] == -1:  # If the neighbor hasn't been colored yet
#                         color[neighbor] = 1 - current_color  # Color with opposite color
#                         queue.append(neighbor)
#                     elif color[neighbor] == current_color:  # If the neighbor has the same color
#                         return False

#     return True

# def main():
#     K = int(input().strip())

#     for _ in range(K):
#         V, E = map(int, input().strip().split())
#         graph = [[] for _ in range(V + 1)]
        
#         for _ in range(E):
#             u, v = map(int, input().strip().split())
#             graph[u].append(v)
#             graph[v].append(u)
        
#         if is_bipartite(V, graph):
#             print("YES")
#         else:
#             print("NO")

# if __name__ == "__main__":
#     main()


