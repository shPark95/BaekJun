# 18258 큐2
from typing import Any

class FixedQueue:
    class Empty(Exception):
        pass
    class Full(Exception):
        pass
    def __init__(self, capacity:int) -> None:
        self.no = 0
        self.rear = 0
        self.front = 0
        self.capacity = capacity
        self.que = [None]*capacity
    def __len__(self) -> int:
        return self.no
    def is_empty(self) -> bool:
        return self.no <= 0
    def is_full(self) -> bool:
        return self.no >= self.capacity
    def enque(self, x:Any) -> None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0
    def deque(self) -> Any:
        if self.is_empty():
            return -1
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x
    def peek_front(self) -> Any:
        if self.is_empty():
            return -1
        return self.que[self.front]
    def peek_back(self) -> Any:
        if self.is_empty():
            return -1
        return self.que[self.rear - 1 if self.rear != 0 else self.capacity - 1]

import sys
def main():
    N = int(sys.stdin.readline().strip())
    q = FixedQueue(2000000)
    answer = []
    for _ in range(N):
        order = sys.stdin.readline().strip().split()
        if order[0] == "push":
            q.enque(order[1])
        elif order[0] == "pop":
            answer.append(q.deque())
        elif order[0] == "size":
            answer.append(q.no)
        elif order[0] == "empty":
            answer.append(1 if q.is_empty() else 0)
        elif order[0] == "front":
            answer.append(q.peek_front())
        elif order[0] == "back":
            answer.append(q.peek_back())
    
    for ans in answer:
        print(ans)

if __name__ == "__main__":
    main()