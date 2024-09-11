import sys
import math
from collections import deque

# 입력
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])
broken_stones = set(int(data[i]) for i in range(2, 2 + m))

# dp 테이블 정의
dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
dp[1][0] = 0  # 시작점

# 바텀업 방식으로 DP 테이블 채우기
for i in range(1, n + 1):
    if i in broken_stones:
        continue
    for last_jump in range(n + 1):
        if dp[i][last_jump] == float('inf'):
            continue
        # 가능한 점프 크기 (last_jump-1), (last_jump), (last_jump+1)
        for jump in [last_jump - 1, last_jump, last_jump + 1]:
            if jump < 0:
                continue
            next_pos = i + jump
            if next_pos > n or next_pos in broken_stones:
                continue
            dp[next_pos][jump] = min(dp[next_pos][jump], dp[i][last_jump] + 1)

# 결과 출력
result = min(dp[n])
if result == float('inf'):
    print(-1)
else:
    print(result)