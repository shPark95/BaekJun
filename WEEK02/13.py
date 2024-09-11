# 3190 뱀
from collections import deque
import sys
N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())
apples = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(K)]
L = int(sys.stdin.readline().strip())
turns = [sys.stdin.readline().strip().split() for _ in range(L)]
dx = [0,1,0,-1] # 우 하 좌 상
dy = [1,0,-1,0]

snake_map = [[0]*N for _ in range(N)]
for x, y in apples:
    snake_map[x-1][y-1] = 1

snake = deque([(0, 0)])
direction = 0   # 우0 하1 좌2 상3
time = 0
direction_index=0

while True:
    time += 1

    head_x, head_y = snake[0]
    new_x = head_x + dx[direction]
    new_y = head_y + dy[direction]

    # 벽에 부딪히거나 몸에 부딪히면 게임 종료
    if not (0 <= new_x < N and 0 <= new_y < N) or (new_x, new_y) in snake:
        break
    
    # 새로운 머리 위치 추가
    snake.appendleft((new_x, new_y))

    # 사과가 있으면 먹고, 없으면 꼬리 자르기
    if snake_map[new_x][new_y] == 1:
        snake_map[new_x][new_y] = 0
    else:
        snake.pop()

    # 방향 전환 처리
    if direction_index < L and time == int(turns[direction_index][0]):
        if turns[direction_index][1] == 'L':
            direction = (direction - 1) % 4  # 왼쪽으로 회전
        else:
            direction = (direction + 1) % 4  # 오른쪽으로 회전
        direction_index += 1

print(time)