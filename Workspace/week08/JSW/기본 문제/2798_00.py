# Problem: 블랙잭(https://www.acmicpc.net/problem/2798)
# Algorithm: Brute Force
# Big-O: N**3

N, M = map(int, input().split())
cards = list(map(int, input().split()))
target = -1
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            temp = cards[i] + cards[j] + cards[k]
            if temp <= M:
                target = max(target, temp)

print(target)