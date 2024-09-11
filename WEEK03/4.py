# 2624 동전 바꿔주기

import sys
input = sys.stdin.readline

T=int(input().strip())
K=int(input().strip())

coins = []
for i in range(K):
    price, n = map(int, input().split())
    coins.append((price, n))
coins.sort(reverse=True)

dp = [0] * (T+1)
dp[0] = 1
#dp뜻은 가격인덱스, 최대 방법수
for j in range(K):
    p, c = coins[j]
    for i in range(T, 0, -1):
        for k in range(1, c+1):
            if i-p*k >=0:
                dp[i] += dp[i-p*k]

    
print(dp[T])













# coins = []
# for _ in range(K):
#     coin_value, coin_count = map(int, input().split())
#     coins.append((coin_value, coin_count))
# coins.sort(key=lambda x: x[0], reverse=True)

# dp = [0] * (T+1)
# dp[0] = 1

# for coin_val, coin_cnt in coins:
#     for i in range(T, coin_val-1, -1):
#         for j in range(1, coin_cnt + 1):
#             if i - coin_val * j >= 0:
#                 dp[i] += dp[i - coin_val * j]
#             else:
#                 break

# print(dp[T])
