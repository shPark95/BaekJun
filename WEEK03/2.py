# 1904 01타일

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())


# # Top-down방식
# dp = [0]*(1000001)
# def fibo(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
    
#     if dp[n] != 0:
#         return dp[n]
    
#     dp[n] = fibo(n-1) + fibo(n-2)

#     return dp[n]


# Bottom-up 방식
dp = [-1]*(1000001)
def fibo(n):

    if N >= 0:
        dp[0] = 1
    if N >= 1:
        dp[1] = 1
    
    if N >= 2:
        for i in range(2, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 15746
            
    return dp[n]

print(fibo(N))