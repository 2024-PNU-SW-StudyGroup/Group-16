# 팩토리얼 2
def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

N = int(input())
print(fact(N))