# Problem: N과 M (2) (https://www.acmicpc.net/problem/15650)
# Date: 2024.11.18
# Comment

def combinations(iterable, r):
    def recurse(iterable, depth, reserved, temp, history):
        if depth == r:
            history.append(temp[::])
            return history
        for i in range(reserved, len(iterable)):
            temp.append(iterable[i])
            recurse(iterable, depth+1, i+1, temp, history)
            temp.pop()
        return history
    return recurse(iterable, 0, 0, [], [])

N, M = map(int, input().split())
print("\n".join(map(
    " ".join, 
    combinations([chr(ord('1') + i) for i in range(N)], M)
)))