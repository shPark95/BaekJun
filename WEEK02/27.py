# 14888 연산자 끼워넣기
import sys

input = sys.stdin.readline

N=int(input().strip())
num_list=list(map(int, input().strip().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num_list[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num_list[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num_list[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num_list[depth]), plus, minus, multiply, divide - 1)


dfs(1, num_list[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)

