# 2178 미로 탐색
from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int, input().strip().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
dx = [0, 1, 0, -1]     #우 하 좌 상
dy = [1, 0, -1, 0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
        
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[N-1][M-1]

print(bfs(0,0))
