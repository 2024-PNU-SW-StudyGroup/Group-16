# 회사에 있는 사람

import sys
input = sys.stdin.readline

n = int(input())
history = set()
for _ in range(n):
    name, state = input().split()
    if name in history: history.remove(name)
    else: history.add(name)
print(*sorted(history, reverse=True), sep='\n')