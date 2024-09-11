from collections import deque, defaultdict

def toy_assembly(N, M, info):
    indegree = [0] * (N + 1)
    graph = defaultdict(list)
    needs = [[0] * (N + 1) for _ in range(N + 1)]
    
    for X, Y, K in info:
        graph[Y].append((X, K))
        indegree[X] += 1
    
    q = deque()
    basic_parts = []
    
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            basic_parts.append(i)
    
    while q:
        current = q.popleft()
        for next_part, count in graph[current]:
            if current in basic_parts:
                needs[next_part][current] += count
            else:
                for i in range(1, N + 1):
                    needs[next_part][i] += needs[current][i] * count
            indegree[next_part] -= 1
            if indegree[next_part] == 0:
                q.append(next_part)
    
    result = []
    for part in basic_parts:
        if needs[N][part] > 0:
            result.append((part, needs[N][part]))
    
    return result

# 입력
N = int(input().strip())  # 부품의 개수
M = int(input().strip())  # 관계의 수
info = [tuple(map(int, input().split())) for _ in range(M)]

# 결과 출력
result = toy_assembly(N, M, info)
for part, count in result:
    print(part, count)