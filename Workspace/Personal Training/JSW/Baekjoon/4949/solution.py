import sys

stack = []
push = lambda x: stack.append(x)
pop = lambda: stack.pop() if stack else False
peek = lambda: stack[-1] if stack else False
pairs = {'(': ')', '[': ']'}
def isVPS(s):
    stack.clear()
    for c in s:
        if c in "([":
            push(c)
        elif c in ")]":
            popped = pop()
            if popped == False or pairs[popped] != c:
                return False
    return not stack

result = []
while (line:= sys.stdin.readline().strip('\n')) != '.':
    result.append('yes' if isVPS(line) else 'no')

print('\n'.join(result))