# Problem: N과 M (1) (https://www.acmicpc.net/problem/15649)
# Date: 2024.11.18
# Comment

def permutation(arr, r):
    def recurse(arr, depth, reserved=None, temp=None, history=None):
        if depth == r:
            history.append(temp[::])
            return history
        for i in range(len(arr)):
            if reserved[i] == 1:
                continue
            temp.append(arr[i])
            reserved[i] = 1
            recurse(arr, depth+1, reserved, temp, history)
            temp.pop()
            reserved[i] = 0
        return history
    return recurse(arr, 0, [0]*(len(arr)), [], [])

N, M = map(int, input().split())
print("\n".join(
    map(" ".join, permutation([chr(ord('1') + i) for i in range(N)], M)
    )
))  