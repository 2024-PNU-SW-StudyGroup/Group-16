# Problem: 곱셈(https://www.acmicpc.net/problem/1629)
# Date: 2024.12.05
# Comment: Naive Approach -> failed
    
A, B, C = map(int, input().split())
A %= C
result = 1
for _ in range(B):
    result *= A
    result %= C
    print(result)
print(result)