import sys
input = sys.stdin.readline

def matrix_chain_order(p):
    n = len(p) - 1  # 행렬의 수
    m = [[0 for _ in range(n)] for _ in range(n)]  # m[i][j]: Ai부터 Aj까지 최소 곱셈 횟수
    s = [[0 for _ in range(n)] for _ in range(n)]  # s[i][j]: Ai부터 Aj까지 최적 분할 위치

    # l은 체인의 길이 (2부터 n까지)
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')  # 무한대 값으로 초기화
            for k in range(i, j):
                # 비용 계산: m[i][k] + m[k+1][j] + Ai-1*Ak*Aj
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

N = int(input().strip())
num_list = []
for _ in range(N):
    r,c = map(int, input().strip().split())
    if not num_list:
        num_list.append(r)
    num_list.append(c)

m, s = matrix_chain_order(num_list)

print(m[0][N-1])
