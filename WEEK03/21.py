# 1541 잃어버린 괄호

from collections import deque
import sys

input = sys.stdin.readline

eq = list(input().strip())
q = deque()

result = 0
num = 0
tmp = 1
for i in range(len(eq)-1, -1, -1):
    if eq[-1] == '-':
        result = abs(result) + num
        result = -result
        num = 0
        tmp = 1
        eq.pop()
    elif eq[-1] == '+':
        result = abs(result) + num
        num = 0
        tmp = 1
        eq.pop()
    elif len(eq) == 1:
        num += int(eq.pop()) * tmp
        result += num
    else:
        num += int(eq.pop()) * tmp
        tmp *= 10

print(result)

# import sys

# input = sys.stdin.readline

# eq = input().strip()

# # '-'로 문자열을 나눔
# parts = eq.split('-')

# # 첫 번째 파트는 무조건 더함
# result = sum(map(int, parts[0].split('+')))

# # 나머지 파트는 모두 빼줌
# for part in parts[1:]:
#     result -= sum(map(int, part.split('+')))

# print(result)