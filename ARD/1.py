# 1259 팰린드롬수

import sys
input = sys.stdin.readline

def is_perindrom():
    while 1:
        result = True
        num = input().strip()
        if num == '0':
            return
        
        n = len(num)
        half = n//2
        for i in range(half):
            if num[i] != num[-1-i]:
                result = False
                break
        if result:
            print('yes')
        else:
            print('no')

is_perindrom()    
