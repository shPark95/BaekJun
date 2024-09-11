# 2294 동전 2

import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())

coins = [int(input().strip()) for _ in range(n)]

dp = [float('inf')] * (k + 1)
dp[0] = 0  # 0원을 만드는 데 필요한 동전 수는 0개
#dp의 의미 = k를 만들기 위해 사용한 최소 동전개수

for i in range(1, k+1):
    min_dp = float('inf')
    for coin in coins:
        if i-coin < 0:
            continue
        if min_dp >= dp[i-coin]:
            min_dp = dp[i-coin]
    dp[i] = min_dp+1

if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])


# # DP 테이블 초기화 (큰 값으로 초기화)
# dp = [float('inf')] * (k + 1)
# dp[0] = 0  # 0원을 만드는 데 필요한 동전 수는 0개

# # DP 수행
# for coin in coins:
#     for i in range(coin, k + 1):
#         dp[i] = min(dp[i], dp[i - coin] + 1)

# # 결과 출력
# if dp[k] == float('inf'):
#     print(-1)
# else:
#     print(dp[k])




# from collections import deque

# def bfs_min_coins(n, k, coins):
#     # DP 배열 초기화 (최소 동전 개수를 저장)
#     visited = [-1] * (k + 1)
#     queue = deque()
    
#     # 시작 상태(0원) 설정
#     queue.append(0)
#     visited[0] = 0
    
#     while queue:
#         current = queue.popleft()
        
#         for coin in coins:
#             next_value = current + coin
            
#             # 목표 금액을 넘는 경우 건너뛰기
#             if next_value > k:
#                 continue
            
#             # 아직 방문하지 않은 경우
#             if visited[next_value] == -1:
#                 visited[next_value] = visited[current] + 1
#                 queue.append(next_value)
    
#     return visited[k]

# # 입력 처리
# n, k = map(int, input().split())
# coins = [int(input()) for _ in range(n)]

# # BFS로 문제 해결
# result = bfs_min_coins(n, k, coins)

# # 결과 출력 (결과가 -1이면, 불가능한 경우)
# print(result if result != -1 else -1)
