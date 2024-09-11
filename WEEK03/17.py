# 12920 평범한 배낭2

import sys
input = sys.stdin.readline

N,M = map(int, input().strip().split())
dp = [0]*(M+1)
items = []
count = 0
for _ in range(N):
    V,C,K = map(int, input().strip().split())

    count = 1
    while K > 0:
        group = min(count, K)
        K -= group
        weight = V * group
        value = C * group
        for j in range(M, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)
        count *= 2

print(dp[M])
    # if K != 1:
    #     for _ in range(K):
    #         count += 1
    #         items.append((V,C))