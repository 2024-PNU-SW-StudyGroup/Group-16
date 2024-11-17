# Problem: 분해합(https://www.acmicpc.net/problem/2231)
# Big-O: NlogN
# Comment: 
# - decomposition(n)을 개선함

def decomposition(n):
    result = n
    while n > 0:
        result += n%10
        n //= 10
    return result

N = int(input())
for i in range(1, N):
    if decomposition(i) == N:
        print(i)
        exit()
print(0)