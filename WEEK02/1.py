# 10828 스택


# import sys

# class FixedStack:
#     def __init__(self, capacity: int = 256) -> None:
#         self.stk = [None] * capacity
#         self.capacity = capacity
#         self.ptr = 0

#     def __len__(self) -> int:
#         return self.ptr

#     def is_empty(self) -> bool:
#         return self.ptr <= 0

#     def is_full(self) -> bool:
#         return self.ptr >= self.capacity

#     def push(self, value: int) -> None:
#         if self.is_full():
#             return  # 스택이 가득 찼을 때는 아무 작업도 하지 않음
#         self.stk[self.ptr] = value
#         self.ptr += 1

#     def pop(self) -> int:
#         if self.is_empty():
#             return -1
#         self.ptr -= 1
#         return self.stk[self.ptr]

#     def peek(self) -> int:
#         if self.is_empty():
#             return -1
#         return self.stk[self.ptr - 1]

# def main():
#     input = sys.stdin.read
#     data = input().splitlines()
#     N = int(data[0])

#     s = FixedStack(64)

#     results = []

#     for i in range(1, N + 1):
#         order = data[i].split()

#         if order[0] == 'push':
#             s.push(int(order[1]))
#         elif order[0] == 'pop':
#             results.append(s.pop())
#         elif order[0] == 'size':
#             results.append(len(s))
#         elif order[0] == 'empty':
#             results.append(1 if s.is_empty() else 0)
#         elif order[0] == 'top':
#             results.append(s.peek())

#     sys.stdout.write("\n".join(map(str, results)) + "\n")

# if __name__ == "__main__":
#     main()

import sys
input = sys.stdin.read

class DynamicStack:
    def __init__(self) -> None:
        self.stk = []
    
    def __len__(self) -> int:
        return len(self.stk)
    
    def is_empty(self) -> bool:
        return len(self.stk) == 0
    
    def push(self, value: int) -> None:
        self.stk.append(value)
    
    def pop(self) -> int:
        if self.is_empty():
            return -1
        return self.stk.pop()
    
    def top(self) -> int:
        if self.is_empty():
            return -1
        return self.stk[-1]

def main():
    data = input().strip().splitlines()
    N = int(data[0])
    
    s = DynamicStack()
    results = []
    
    for i in range(1, N + 1):
        order = data[i].split()
        command = order[0]
        
        if command == 'push':
            s.push(int(order[1]))
        elif command == 'pop':
            results.append(s.pop())
        elif command == 'size':
            results.append(len(s))
        elif command == 'empty':
            results.append(1 if s.is_empty() else 0)
        elif command == 'top':
            results.append(s.top())
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()
