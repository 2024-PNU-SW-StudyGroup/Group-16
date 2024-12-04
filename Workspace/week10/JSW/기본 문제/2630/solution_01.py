# Problem: 색종이 만들기(https://www.acmicpc.net/problem/2630)
# Date: 2024.12.04
# Comment: 

import sys
input = sys.stdin.readline
def check(y, x, n):
    for i in range(y, y+n):
        for j in range(x, x+n):
            if arr[y][x] != arr[i][j]:
                return False
    return True

# WHITE, BLUE = 0, 1
counter = [0] * 2
def count_color(y, x):
    counter[arr[y][x]] += 1

dys = [0, 0, 1, 1]
dxs = [0, 1, 0, 1]
def divide(y, x, n):
    white, blue = 0, 0
    if n == 1:
        count_color(y, x)
        return
    if check(y, x, n):
        count_color(y, x)
        return
    stride = n//2
    for dy, dx in zip(dys, dxs):
        divide(y + dy*stride, x + dx*stride, stride)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

divide(0, 0, N)
print(*counter, sep='\n')
