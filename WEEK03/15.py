# 2169 로봇 조종하기
# 누적합을 dp에 기록
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
region = []
for _ in range(N):
    region.append(list(map(int, input().strip().split())))

dp = [[-float('inf')] * M for _ in range(N)]
dp[0][0] = region[0][0]

# 왼쪽에서 오는 경우
for i in range(1, M):
    dp[0][i] = dp[0][i-1] + region[0][i]

for i in range(1, N):
    left_to_right = [-float('inf')] * M
    right_to_left = [-float('inf')] * M
    
    # 왼쪽에서 오른쪽으로 채우기
    left_to_right[0] = dp[i-1][0] + region[i][0]
    for j in range(1, M):
        left_to_right[j] = max(left_to_right[j-1], dp[i-1][j]) + region[i][j]
    
    # 오른쪽에서 왼쪽으로 채우기
    right_to_left[M-1] = dp[i-1][M-1] + region[i][M-1]
    for j in range(M-2, -1, -1):
        right_to_left[j] = max(right_to_left[j+1], dp[i-1][j]) + region[i][j]
    
    # 두 경우를 비교하여 dp 테이블 업데이트
    for j in range(M):
        dp[i][j] = max(left_to_right[j], right_to_left[j])

print(dp[N-1][M-1])
