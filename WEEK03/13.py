# 1509 팰린드롬 분할

import sys
input = sys.stdin.readline

s=input().strip()
n=len(s)

dp = [[False] * (n+1) for _ in range(n+1)]

# 1. 길이가 1인 경우, 모든 구간은 팰린드롬이다.
for i in range(n):
    dp[i][i] = True

# 2. 길이가 2인 경우, 두 숫자가 같으면 팰린드롬이다.
for i in range(n - 1):
    if s[i] == s[i + 1]:
        dp[i][i + 1] = True

# 3. 길이가 3 이상인 경우, 양 끝이 같고 그 안쪽 구간이 팰린드롬이면 팰린드롬이다.
for length in range(3, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        if s[i] == s[j] and dp[i + 1][j - 1]:
            dp[i][j] = True

# dp[i]는 문자열 s의 처음부터 i번째까지 최소 분할 수
dp2 = [float('inf')] * n

for i in range(n):
    if dp[0][i]:  # 처음부터 i까지가 팰린드롬인 경우
        dp2[i] = 1
    else:
        for j in range(i):
            if dp[j + 1][i]:
                dp2[i] = min(dp2[i], dp2[j] + 1)

# dp[n-1]에는 문자열 전체의 최소 분할 수가 저장됨
print(dp2[-1])