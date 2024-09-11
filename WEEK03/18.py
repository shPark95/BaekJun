# 2098 외판원 순회

import sys
input = sys.stdin.readline

N=int(input().strip())
costs = []
for _ in range(N):
    costs.append(list(map(int, input().strip().split())))

# DP 테이블
dp = [[float('inf')] * N for _ in range(1 << N)]
dp[1][0] = 0

# DP 업데이트
for mask in range(1 << N):
    for u in range(N):
        if not (mask & (1 << u)):
            continue
        for v in range(N):
            if mask & (1 << v):
                continue
            next_mask = mask | (1 << v)
            dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + costs[u][v])

# 최소 비용 계산
result = float('inf')
for u in range(1, N):
    result = min(result, dp[(1 << N) - 1][u] + costs[u][0])

print(result)
