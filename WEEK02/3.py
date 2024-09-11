#  괄호 9012
import sys

def is_valid_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

def main():
    input = sys.stdin.readline
    T = int(input().strip())
    
    results = []
    for _ in range(T):
        s = input().strip()
        result = is_valid_parentheses(s)
        results.append(result)
    
    print("\n".join(results))

if __name__ == "__main__":
    main()