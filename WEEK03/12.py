# 10942 팰린드롬

import sys
input = sys.stdin.readline

N = int(input().strip())
num_list=list(map(int, input().strip().split()))
M = int(input().strip())
data = []
for _ in range(M):
    S, E = map(int, input().strip().split())
    data.append((S,E))

dp = [[False] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = True

for i in range(N-1):
    if num_list[i] == num_list[i+1]:
        dp[i][i+1] = True

for length in range(3, N+1):
    for i in range(N-length+1):
        j=i+length-1
        if num_list[i] == num_list[j] and dp[i+1][j-1]:
            dp[i][j]=True










# 1. 길이가 1인 경우, 모든 구간은 팰린드롬이다.
for i in range(N):
    dp[i][i] = True

# 2. 길이가 2인 경우, 두 숫자가 같으면 팰린드롬이다.
for i in range(N - 1):
    if num_list[i] == num_list[i + 1]:
        dp[i][i + 1] = True

# 3. 길이가 3 이상인 경우, 양 끝이 같고 그 안쪽 구간이 팰린드롬이면 팰린드롬이다.
for length in range(3, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1
        if num_list[i] == num_list[j] and dp[i + 1][j - 1]:
            dp[i][j] = True

# 쿼리 처리
result = []
for S, E in data:
    # S와 E는 1-based index이므로, 0-based index로 변환해 사용
    if dp[S - 1][E - 1]:
        result.append(1)
    else:
        result.append(0)

# 결과 출력
print("\n".join(map(str, result)))
