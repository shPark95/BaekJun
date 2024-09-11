# 11866 요세푸스
from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N + 1))
result = []

while len(queue) != 1:
    queue.rotate(-K+1)
    result.append(queue.popleft())

print("<"+", ".join(map(str, result)) + ">")
