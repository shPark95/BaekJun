# 18352 특정 거리의 도시 찾기
from collections import deque
import sys
input = sys.stdin.readline

N,M,K,X = map(int, input().strip().split())
graph = {i:[] for i in range(1, N+1)}
distance = [-1] * (N + 1)  # 모든 도시의 거리를 -1로 초기화
distance[X] = 0  # 출발 도시의 거리는 0으로 설정

def bfs(start):
    queue = deque([start])
    while queue:
        v=queue.popleft()
        for next_city in graph[v]:
            if distance[next_city] == -1:
                distance[next_city] = distance[v] + 1
                queue.append(next_city)
    
for _ in range(M):
    A, B = map(int, input().strip().split())
    graph[A].append(B)

bfs(X)

result = []
for i in range(1, N + 1):
    if distance[i] == K:
        result.append(i)
        
if result:
    result.sort()
    for city in result:
        print(city)
else:
    print(-1)

