T = int(input())
for _ in range(T):
    stack = []
    is_vps = True
    line = input()
    for c in line:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                is_vps = False
                break
            stack.pop()
    if stack:
        is_vps = False
    print('YES' if is_vps else 'NO')