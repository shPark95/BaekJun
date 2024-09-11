# 11053 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

N=int(input().strip())
A=list(map(int, input().strip().split()))

def length_of_lis(nums):
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

print(length_of_lis(A))

