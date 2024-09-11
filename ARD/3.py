# 18126 너구리 구구

from collections import defaultdict
import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
distance = [float('-inf')]*(N+1)
graph = defaultdict(list)
for _ in range(N-1):
    u, v, w = map(int, input().strip().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(start, end):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cur_cost, cur_node = heapq.heappop(queue)
        if distance[cur_node] > cur_cost:
            continue
        for adj_node, adj_cost in graph[cur_node]:
            cost = cur_cost-adj_cost
            if cost>distance[adj_node]:
                distance[adj_node]=cost
                heapq.heappush(queue, (cost, adj_node))
    return distance[end]

maxcost = 0
for i in range(1, N+1):
    maxcost = min(maxcost, dijkstra(1, i))

print(-maxcost)