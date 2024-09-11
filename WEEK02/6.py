#2493 탑

import sys
N=int(sys.stdin.readline().strip())
towers = list(map(int, sys.stdin.readline().strip().split()))

result = [0]*N
stack=[]

for i in range(N):
    while stack and stack[-1][1] < towers[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1][0] +1
    stack.append((i, towers[i]))

print(' '.join(map(str, result)))

for i in range(N):
    towers[i]