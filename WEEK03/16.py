# 12865 평범한 배낭

import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
data = []
for _ in range(N):
    W, V = map(int, input().strip().split())
    data.append((W,V))

# dp 테이블 초기화
dp = [[0] * (K + 1) for _ in range(N + 1)]

# 동적 프로그래밍 진행
for i in range(1, N + 1):
    weight, value = data[i-1]
    for j in range(1, K + 1):
        if j >= weight:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
        else:
            dp[i][j] = dp[i-1][j]

# 결과 출력
print(dp[N][K])

# # dp 테이블 초기화
# dp = [0] * (k + 1)

# # 동적 프로그래밍 진행
# for weight, value in items:
#     for i in range(k, weight - 1, -1):
#         dp[i] = max(dp[i], dp[i - weight] + value)

# # 결과 출력
# print(dp[k])