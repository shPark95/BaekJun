# 9252 LCS 2
# import sys
# sys.setrecursionlimit(10**6)

# input = sys.stdin.readline

# s1 = input().strip()
# s2 = input().strip()
# m = len(s1)
# n = len(s2)

# b = [[0]*(n+1) for i in range(m+1)] # 1:좌상 2:상 3:좌
# c = [[0]*(n+1) for i in range(m+1)]

# def lcs(m,n):
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             if s1[i-1] == s2[j-1]:
#                 c[i][j]=c[i-1][j-1]+1
#                 b[i][j]=1
#             elif c[i-1][j] >= c[i][j-1]:
#                 c[i][j]=c[i-1][j]
#                 b[i][j]=2
#             else:
#                 c[i][j]=c[i][j-1]
#                 b[i][j]=3
#     return c, b

# def print_lcs(b,s1,i,j):
#     if i==0 or j==0:
#         return
#     if b[i][j]== 1:
#         print_lcs(b,s1,i-1,j-1)
#         print(s1[i-1], end='')
#     elif b[i][j]== 2:
#         print_lcs(b,s1,i-1,j)
#     else:
#         print_lcs(b,s1,i,j-1)

# c, b = lcs(m,n)
# print(c[m][n])
# print_lcs(b, s1, m, n)

import sys
input = sys.stdin.readline

A = ['']+list(input().strip())
B = ['']+list(input().strip())
LCS = [['']*len(B) for _ in range(len(A))]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            LCS[i][j] = LCS[i-1][j-1]+A[i]
        else:
            if len(LCS[i-1][j]) >= len(LCS[i][j-1]):
                LCS[i][j] = LCS[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]




A = [""] + list(input().rstrip())
B = [""] + list(input().rstrip())
LCS = [[""]*len(B) for _ in range(len(A))]

# LCS[i][j]는 A의 i번째까지의 문자열과
# B의 j번째까지의 문자열의 LCS 길이 값을 의미함
# LCS[i][j]에서, 만약 A[i] == B[j]라면
# 그 두 문자를 제외한 i-1개, j-1개의 LCS
# 만약 다르다면, i-1개, j개와 i개, j-1개
# 일 때의 LCS 중 큰 값 취하기. i-1개, j-1개
# 는 어차피 저 두 케이스보다 반드시 작거나 같으므로
# 두 케이스만 고려.
# 그런데 LCS 리스트 원소 값이 LCS 길이 값을 의미하므로,
# 원소를 LCS 문자열 자체로 둬도 됨. 그럼 길이 값도 갖고
# 최단 경로도 갖고 있게 됨.
for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            LCS[i][j] = LCS[i-1][j-1] + A[i]
        else:
            if len(LCS[i-1][j]) >= len(LCS[i][j-1]):
                LCS[i][j] = LCS[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]

result = LCS[-1][-1]
print(len(result), result, sep="\n")