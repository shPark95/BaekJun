# 1781 컵라면

import heapq
import sys
input = sys.stdin.readline

N = int(input().strip())
table = []
for _ in range(N):
    D, C = map(int, input().strip().split())
    table.append((D, C))  
table.sort()

pq = []
for i in table:
    heapq.heappush(pq, i[1])
    if i[0] < len(pq):
        heapq.heappop(pq)

print(sum(pq))
