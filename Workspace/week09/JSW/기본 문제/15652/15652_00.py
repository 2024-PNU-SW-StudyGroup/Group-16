# Problem: N과 M (4) (https://www.acmicpc.net/problem/15652)
# Date: 2024.11.18
# Comment

from itertools import combinations_with_replacement
N, M = map(int, input().split())
print("\n".join(map(" ".join, combinations_with_replacement([chr(ord('1') + i) for i in range(N)], M))))