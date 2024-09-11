#제로
import sys

K=int(sys.stdin.readline().strip())
stk = []

while K>0:
    K-=1
    JH=int(sys.stdin.readline().strip())

    if JH==0:
        stk.pop()
    else:
        stk.append(JH)

    print(sum(stk))