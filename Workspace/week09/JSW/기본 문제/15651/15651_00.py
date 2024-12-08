# Problem: N과 M (3) (https://www.acmicpc.net/problem/15651)
# Date: 2024.11.18
# Comment

from itertools import product
N, M = map(int, input().split())
print("\n".join(map(" ".join, product([chr(ord('1') + i) for i in range(N)], repeat=M))))