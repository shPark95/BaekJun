# 2665 미로만들기
import heapq
import sys
input = sys.stdin.readline

n = int(input().strip())
maze = [list(map(int, input().strip())) for _ in range(n)]
cost = [[float('inf')]*n for _ in range(n)]
cost[0][0] = 0

dx = [0, 1, 0, -1]    #우 하 좌 상
dy = [1, 0, -1, 0]

pq = []
heapq.heappush(pq, (0, 0, 0))

def dijkstra():
    while pq:
        current_cost, r, c = heapq.heappop(pq)
        if current_cost > cost[r][c]:
            continue

        for i in range(4):
            nx = r+dx[i]
            ny = c+dy[i]

            if 0<=nx<n and 0<=ny<n:
                # 다음 방이 흰 방이라면
                new_cost = current_cost if maze[nx][ny] == 1 else current_cost + 1
                
                # 새로운 비용이 더 적다면 갱신 후 큐에 추가
                if new_cost < cost[nx][ny]:
                    cost[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))

    return cost[n-1][n-1]

print(dijkstra())


