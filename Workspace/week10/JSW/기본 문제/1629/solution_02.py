# Problem: 곱셈(https://www.acmicpc.net/problem/1629)
# Date: 2024.12.04
# Comment: Naive Approach -> failed
    
A, B, C = map(int, input().split())
A %= C
result = 1
history = []
history_set = set()
multiple = 1
for i in range(B):
    result *= A
    result %= C
    if result in history_set:
        multiple = i + 1
        break
    history.append(result)
    history_set.add(result)

print(history[B % multiple - 1]) if multiple != 1 else print(result)