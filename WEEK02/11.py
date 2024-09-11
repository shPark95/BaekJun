# 2164 카드2
from collections import deque
import sys

N = int(sys.stdin.readline().strip())
q = deque(range(1, N + 1))

while len(q) > 1:
    q.popleft()           # 첫 번째 카드를 버림
    q.append(q.popleft()) # 두 번째 카드를 큐의 맨 뒤로 이동

print(q[0])

# N = int(sys.stdin.readline().strip())
# que = [i for i in range(1, N+1)]

# while len(que) > 1:
#     que.remove(que[0])
#     que.append(que.pop(0))

# for i in que:
#     print(i)
