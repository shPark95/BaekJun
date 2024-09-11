# 2629 양팔저울

import sys
input = sys.stdin.readline

nweight = int(input().strip())
weight_list = list(map(int, input().strip().split()))
nbead = int(input().strip())
bead_list = list(map(int, input().strip().split()))

maxweight = sum(weight_list)

def weight_check():
    dp = [False]*(maxweight+1)
    dp[0] = True

    for weight in weight_list:
        for j in range(maxweight, -1, -1):
            if dp[j]:
                dp[j + weight] = True
                dp[abs(j - weight)] = True

    for bead in bead_list:
        if bead > maxweight:
            print('N', end=' ')
        elif dp[bead]:
            print('Y', end=' ')
        else:
            print('N', end=' ')

weight_check()



# def check_weight():
#     dpweight = [False] * (maxweight+1)
#     dpweight[0] = True
#     for weight in weight_list:
#         new_dp = dpweight[:]
#         for i in range(maxweight + 1):
#             if dpweight[i]:
#                 # 추가를 왼쪽에 올린 경우
#                 if i + weight <= maxweight:
#                     new_dp[i + weight] = True
#                 # 추가를 오른쪽에 올린 경우
#                 if abs(i - weight) <= maxweight:
#                     new_dp[abs(i - weight)] = True
#         dpweight = new_dp

#     results = []
#     for bead in bead_list:
#         if bead > maxweight:
#             results.append("N")
#         elif dpweight[bead]:
#             results.append("Y")
#         else:
#             results.append("N")

#     print(' '.join(results))

# check_weight()