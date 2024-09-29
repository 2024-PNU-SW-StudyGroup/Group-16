#반복문을 사용하여 0부터 n까지의 합 풀어보기
n = int(input())
result = 0
for i in range(n):
    result+=(i+1)
print(result)