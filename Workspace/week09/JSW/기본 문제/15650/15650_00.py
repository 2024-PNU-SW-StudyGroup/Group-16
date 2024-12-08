# Problem: N과 M (2) (https://www.acmicpc.net/problem/15650)
# Date: 2024.11.18
# Comment

from itertools import combinations
N, M = map(int, input().split())
print("\n".join(map(" ".join, combinations([chr(ord('1') + i) for i in range(N)], M))))