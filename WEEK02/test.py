import heapq
import sys
input=sys.stdin.readline

N,M=map(int, input().strip().split)
graph = {i:[] for i in range(1, N+1)}
in_count = [0] * (N+1)
pq = []

for _ in range(M):
    A, B = map(int, input().strip().split)
    graph[A].append(B)

for i in range(N):
    in_count[i] = graph[i]
