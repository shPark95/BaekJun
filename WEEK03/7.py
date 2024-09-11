# 9251 LCS
# import sys

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
# # print_lcs(b, s1, m, n)



import sys
input = sys.stdin.readline

A = "0" + input().rstrip()
B = "0" + input().rstrip()

# A가 행, B가 열
LCS = [[0]*len(B) for _ in range(len(A))]

for row in range(1, len(A)):
    for col in range(1, len(B)):
        if A[row] == B[col]:
            LCS[row][col] = LCS[row-1][col-1] + 1
        else:
            LCS[row][col] = max(LCS[row-1][col], LCS[row][col-1])

print(LCS[-1][-1])