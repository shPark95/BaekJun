# 17608 막대기

import sys

N=int(sys.stdin.readline().strip())
polls=[int(sys.stdin.readline().strip()) for _ in range(N)]

stk = []

for poll in polls:
    while stk and stk[-1] <= poll:
        stk.pop()
    stk.append(poll)
print(len(stk))