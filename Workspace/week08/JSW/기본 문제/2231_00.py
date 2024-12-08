# Problem: 분해합(https://www.acmicpc.net/problem/2231)
# Big-O: NlogN
# Comment: 

def decomposition(n):
    return n + sum(map(int, str(n)))

N = int(input())
for i in range(1, N):
    if decomposition(i) == N:
        print(i)
        exit()
print(0)