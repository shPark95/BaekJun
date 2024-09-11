# # 6549 히스토그램에서 가장 큰 사각형
# import sys

# max_list = []
# while True:
#     h = list(map(int, sys.stdin.readline().strip().split()))
#     if h[0] == 0:
#         break
    
#     stack = []
#     max_result = 0

#     for i in range(1, h[0]+1):
#         if stack and stack[-1][1] > h[i]:

#             while stack:  # 스택에서 빼내며 최대 직사각형 넓이를 계산합니다.
#                 stack_i, stack_height = stack.pop()
#                 width_start = 1
#                 if stack:
#                     width_start = stack[-1][0]+1
#                 result = (i - width_start) * stack_height
#                 max_result = max(result, max_result) # 최대값 갱신
#                 # 스택에 들어있는 막대 중에서 현재 막대의 길이보다 큰 것들만 꺼내서 계산합니다.
#                 if not stack or stack[-1][1] <= h[i]:
#                     break

#         # 스택이 비어 있거나 스택의 가장 위쪽 막대기보다 현재 막대기의 높이가 크거나 같으면
#         if not stack or stack[-1][1] <= h[i]:
#             stack.append((i, h[i]))  # 스택에 현재 막대기를 추가합니다.

#     # 반복이 종료되고, 스택에 남은 막대기가 있다면 계산합니다.
#     while stack:
#         stack_i, stack_height = stack.pop()
#         width_start = 1
#         if stack:
#             width_start = stack[-1][0]+1
#         result = (h[0]+1 - width_start) * stack_height
#         max_result = max(result, max_result) # 최대값 갱신
    
#     max_list.append(max_result)

# for i in max_list: 
#     print(i)



import sys
input = sys.stdin.readline


def solution(nums):
    res = 0

    length = nums[0]
    stack = [0]  # 인덱스를 저장
    nums[0] = 0  # 반복문 초기에 nums[stack[0]], 즉 nums[0]과 값을 비교하는데, 이에 대한 처리임
    nums.append(0)  # 마지막 인덱스에서의 연산을 위함

    for i in range(1, length+2):
        while nums[stack[-1]] > nums[i]:
            index = stack.pop()
            res = max(res, (i - (stack[-1] + 1))*nums[index])

        stack.append(i)

    return res


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    while nums[0] != 0:
        print(solution(nums))
        nums = list(map(int, input().split()))