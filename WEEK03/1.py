# 2748 피보나치 수2

import sys
input = sys.stdin.readline

N=int(input().strip())

# Top-down방식
dp = [0]*(N+1)
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if dp[n] != 0:
        return dp[n]
    
    dp[n] = fibo(n-1) + fibo(n-2)

    return dp[n]


# Bottom-up 방식
# dp = [-1]*(N+1)
# def fibo(n):

#     if N >= 0:
#         dp[0] = 0
#     if N >= 1:
#         dp[1] = 1
    
#     if N >= 2:
#         for i in range(2, n+1):
#             dp[i] = dp[i-1] + dp[i-2]
            
#     return dp[n]

print(fibo(N))
