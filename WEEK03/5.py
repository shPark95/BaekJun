# 9084 동전
import sys
input = sys.stdin.readline

def cal_dp(dp, costs, count, total):
    for i in range(count):
        for t in range(costs[i], total + 1):
            dp[t] += dp[t - costs[i]]
    return dp[total]

tcase = int(input().strip())
for _ in range(tcase):
    N = int(input().strip())
    costs = list(map(int, input().strip().split()))
    total = int(input().strip())

    dp = [0] * (total+1)
    dp[0] = 1
    result = cal_dp(dp, costs, N, total)

    print(result)
