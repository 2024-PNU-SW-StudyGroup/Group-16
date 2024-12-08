# 숫자 카드

N = int(input())
sanggeun = set(map(int, input().split()))
M = int(input())
for e in map(int, input().split()):
    if e in sanggeun: print('1', end=' ')
    else: print('0', end=' ')