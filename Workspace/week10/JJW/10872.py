'''def factorial(N):
    if N == 1:
        return 1
    else:
        return N * factorial(N - 1)
    
print(factorial(int(input())))''' # 이거 왜 런타임 에러가 나지

num = int(input())
i = 1
result = 1
while i < num + 1:
    result = result * i
    i += 1

print(result)