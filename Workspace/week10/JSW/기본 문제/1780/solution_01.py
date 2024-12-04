# Problem: 종이의 개수(https://www.acmicpc.net/problem/1780)
# Date: 2024.12.04
# Comment: 

from itertools import product
import sys
input = sys.stdin.readline
def check(y, x, n):
    for i in range(y, y+n):
        for j in range(x, x+n):
            if arr[y][x] != arr[i][j]:
                return False
    return True


counter = {
    -1:0,
    0:0,
    1:0
}
def count_color(y, x):
    counter[arr[y][x]] += 1

dir_map = list(product(range(3), repeat=2))
def divide(y, x, n):
    if n == 1:
        count_color(y, x)
        return
    if check(y, x, n):
        count_color(y, x)
        return
    stride = n//3
    print(stride)
    for dy, dx in dir_map:
        divide(y + dy*stride, x + dx*stride, stride)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

divide(0, 0, N)
print(*counter.values(), sep='\n')