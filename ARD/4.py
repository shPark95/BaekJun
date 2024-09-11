# 7983 내일 할거야

import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())
pq = []
maxvacation = 0
restvacation = 0
for _ in range(n):
    d, t = map(int, input().strip().split())
    heapq.heappush(pq, (t-d, t))
    maxvacation = max(maxvacation, t)

restvacation = (maxvacation + pq[0][0], pq[0][0])
while pq:
    cur_d, cur_t = heapq.heappop(pq)
    if maxvacation >= cur_t:
        maxvacation = cur_t
        maxvacation += cur_d
    else:
        rest_d, rest_t = restvacation
        if rest_t <= cur_t + cur_d and -rest_d >= -cur_d:
            restvacation = (rest_d + cur_d, rest_t)
        else:
            maxvacation += cur_d

print(maxvacation)
