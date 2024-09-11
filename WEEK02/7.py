# 2812 크게 만들기

import sys

N, K = map(int, sys.stdin.readline().strip().split())
num = list(sys.stdin.readline().strip())

stack=[]

removecnt = 0
for i in range(N):
    while removecnt<K and stack and int(stack[-1]) < int(num[i]):
        stack.pop()
        removecnt+=1
    stack.append(num[i])
    
while removecnt < K:
    stack.pop()
    removecnt+=1

print(''.join(stack))