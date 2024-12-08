# Problem: N과 M (4) (https://www.acmicpc.net/problem/15652)
# Date: 2024.11.18
# Comment

def combinations_with_replacement(iterable, r):
    def recurse(iterable, r, reserved, temp, history):
        if r == 0:
            history.append(temp[::])
            return history
        for i in range(reserved, len(iterable)):
            temp.append(iterable[i])
            recurse(iterable, r-1, i, temp, history)
            temp.pop()
        return history
    return recurse(iterable, r, 0, [], [])
N, M = map(int, input().split())
print("\n".join(map(" ".join, combinations_with_replacement([chr(ord('1') + i) for i in range(N)], M))))