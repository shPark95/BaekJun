# 1931 회의실 배정

import sys
input = sys.stdin.readline

N = int(input().strip())

meetings = []
for _ in range(N):
    start, end = map(int, input().strip().split())
    meetings.append((start, end))

# 끝나는 시간을 기준으로 회의를 정렬 (같은 시간일 경우 시작 시간을 기준으로 추가 정렬)
meetings.sort(key=lambda x: (x[1], x[0]))

# 그리디 알고리즘을 적용하여 최대 회의 수 찾기
count = 0
last_end_time = 0

for start, end in meetings:
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)


# # DP 테이블 초기화
# dp = [0] * N
# dp[0] = 1  # 첫 번째 회의를 선택했을 때 회의 수는 1

# for i in range(1, N):
#     # 현재 회의를 선택하지 않는 경우
#     dp[i] = dp[i-1]
    
#     # 현재 회의를 선택하는 경우
#     for j in range(i-1, -1, -1):
#         if meetings[j][1] <= meetings[i][0]:
#             dp[i] = max(dp[i], dp[j] + 1)
#             break
#     else:
#         dp[i] = max(dp[i], 1)  # 이 회의를 포함하더라도 선택할 수 있는 이전 회의가 없는 경우

# # 최대 회의 수 출력
# print(dp[-1])