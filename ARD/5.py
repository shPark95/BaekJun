# 13975 파일합치기3

import sys
import heapq
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    K = int(input().strip())
    filesizes = list(map(int, input().strip().split()))
    heapq.heapify(filesizes)
    
    result = 0
    while len(filesizes) > 1:
        a = heapq.heappop(filesizes)
        b = heapq.heappop(filesizes)
        result += (a + b)
        heapq.heappush(filesizes, a+b)
    
    print(result)
        
    