# 1946 신입 사원

import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N= int(input().strip())
    data=[]
    for _ in range(N):
        A, B = map(int, input().strip().split())
        data.append((A,B))
    data.sort(key=lambda x: x[0])

    # 면접 순위의 최솟값을 기록
    min_interview_rank = data[0][1]
    count = 1
    
    # 두 번째 지원자부터 시작
    for i in range(1, N):
        if data[i][1] < min_interview_rank:
            count += 1
            min_interview_rank = data[i][1]

    print(count)

    # fail = [False] * N
    # for i in range(N):
    #     for score, meet in data:
    #         if data[i][0] > score and data[i][1] > meet:
    #             fail[i] = True

    # print(len(data) - sum(fail))