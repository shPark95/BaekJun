# 5545 최고의 피자
from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input().strip())
A, B = map(int, input().strip().split())
C = int(input().strip())
D = [int(input().strip()) for _ in range(N)]
D.sort(reverse=True)
# result = 0
# for i in range(1, N+1):
#     for j in combinations(D, i):
#         calori = C + sum(j)
#         price = A + B*i
#         result = max(result, calori//price)

price = 0
for i in range(N+1):  
    price = max(price, (C + sum(D[:i]))//(A+B*i))

print(price)
