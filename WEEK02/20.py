# 1197 최소 스패닝 트리
import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def kruskal(v, edges):
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(v + 1)]
    rank = [0] * (v + 1)
    
    mst_weight = 0
    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_weight += weight
    
    return mst_weight

def main():
    v_count,e_count = map(int, input().split())
    edges = []
    
    for _ in range(e_count):
        u, v, weight = map(int, input().split())
        edges.append((u, v, weight))
    
    result = kruskal(v_count, edges)
    print(result)

if __name__ == "__main__":
    main()


# import sys
# import heapq

# def prim(start, graph, v):
#     mst_weight = 0
#     visited = [False] * (v + 1)
#     min_heap = [(0, start)]  # (cost, vertex)
    
#     while min_heap:
#         weight, u = heapq.heappop(min_heap)
        
#         if visited[u]:
#             continue
        
#         mst_weight += weight
#         visited[u] = True
        
#         for next_weight, v in graph[u]:
#             if not visited[v]:
#                 heapq.heappush(min_heap, (next_weight, v))
    
#     return mst_weight

# def main():
#     input = sys.stdin.read
#     data = input().split()
#     v = int(data[0])
#     e = int(data[1])
#     graph = [[] for _ in range(v + 1)]
    
#     idx = 2
#     for _ in range(e):
#         u = int(data[idx])
#         v = int(data[idx + 1])
#         weight = int(data[idx + 2])
#         graph[u].append((weight, v))
#         graph[v].append((weight, u))
#         idx += 3
    
#     # Prim 알고리즘 실행, 임의의 시작점을 1번 노드로 설정
#     result = prim(1, graph, v)
#     print(result)

# if __name__ == "__main__":
#     main()