# 1916 최소비용 구하기

import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
graph = defaultdict(list)
distance = [float('inf')] * (N+1)

def dijkstra(start, end):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cur_cost, cur_node = heapq.heappop(queue)
        if distance[cur_node] < cur_cost:   # 현재 코스트가 최소누적코스트보다 크면 건너뜀
            continue
        for adj_node, adj_cost in graph[cur_node]:
            cost = cur_cost+adj_cost
            if cost<distance[adj_node]:     # 현재 최소누적코스트+주변노드코스트값이 주변노드의 최소누적코스트보다 작은경우
                distance[adj_node]=cost
                heapq.heappush(queue, (cost, adj_node))
    return distance[end]

for i in range(M):
    u,v,w = map(int, input().strip().split())
    graph[u].append((v, w))

start, end = map(int, input().split())
result = dijkstra(start, end)
print(result)

