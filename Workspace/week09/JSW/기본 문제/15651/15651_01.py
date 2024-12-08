# Problem: N과 M (3) (https://www.acmicpc.net/problem/15651)
# Date: 2024.11.18
# Comment

def product(iterable, repeat):
    def recurse(iterable, r, temp, history):
        if r == 0:
            history.append(temp[::])
            return history
        for e in iterable:
            temp.append(e)
            recurse(iterable, r-1, temp, history)
            temp.pop()
        return history
    return recurse(iterable, repeat, [], [])

N, M = map(int, input().split())
print("\n".join(map(" ".join, product([chr(ord('1') + i) for i in range(N)], repeat=M))))