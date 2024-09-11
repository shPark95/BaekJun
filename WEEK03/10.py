# 16500 문자열 판별

import sys
input = sys.stdin.readline

S=input().strip()
N=int(input().strip())

def can_construct(s, word_set):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]

s = input().strip()
n = int(input().strip())
substrings = set(input().strip() for _ in range(n))

# 결과 출력
if can_construct(s, substrings):
    print(1)
else:
    print(0)


