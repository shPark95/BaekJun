# 11279 최대 힙

import heapq
import sys

input = sys.stdin.readline
n = int(input())
operations = [int(input()) for _ in range(n)]

max_heap = []
results = []

for operation in operations:
    if operation != 0:
        heapq.heappush(max_heap, -operation)
    else:
        if max_heap:
            results.append(-heapq.heappop(max_heap))
        else:
            results.append(0)

for i in results:
    print(i)