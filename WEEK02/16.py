# 1715 카드 정렬하기
import heapq
import sys

N= int(sys.stdin.readline().strip())
result = 0
card_list = [int(sys.stdin.readline().strip()) for _ in range(N)]

heapq.heapify(card_list)
total_cost = 0

while len(card_list) > 1:
    first = heapq.heappop(card_list)
    second = heapq.heappop(card_list)

    total_cost = first + second
    heapq.heappush(card_list, total_cost)
    













heapq.heapify(card_list)
total_cost = 0

while len(card_list) > 1:
    first = heapq.heappop(card_list)
    second = heapq.heappop(card_list)

    current_cost = first+second
    total_cost += current_cost

    heapq.heappush(card_list, current_cost)

print(total_cost)
