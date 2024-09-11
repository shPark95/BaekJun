# 11047 동전 0

import sys
input = sys.stdin.readline

N,K = map(int, input().strip().split())
costs = [int(input().strip()) for _ in range(N)]

count = 0
for i in range(N):
    count += K // costs[-1-i]
    K %= costs[-1-i]

print(count)
