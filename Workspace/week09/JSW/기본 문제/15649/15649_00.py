# Problem: N과 M (1) (https://www.acmicpc.net/problem/15649)
# Date: 2024.11.18
# Comment

from itertools import permutations
N, M = map(int, input().split())
print("\n".join(map(" ".join, permutations([chr(ord('1') + i) for i in range(N)], M))))