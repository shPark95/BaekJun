# 1655 가운데를 말해요

import heapq
import sys
input = sys.stdin.readline
N = int(input())
highestq = []
lowestq = []

def baek():
    for _ in range(N):
        num = int(sys.stdin.readline().strip())
        
        if len(lowestq) == len(highestq):
            heapq.heappush(lowestq, -num)
        else:
            heapq.heappush(highestq, num)
        
        if highestq and (-lowestq[0] > highestq[0]):
            left_val = -heapq.heappop(lowestq)
            right_val = heapq.heappop(highestq)
            heapq.heappush(lowestq, -right_val)
            heapq.heappush(highestq, left_val)
        
        print(-lowestq[0])

baek()