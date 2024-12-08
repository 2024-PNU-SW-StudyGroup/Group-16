# Problem: 설탕 배달(https://www.acmicpc.net/problem/2839)
# Comment: 

N = int(input())
for i in range(N//5, -1, -1):
    for j in range(N//3, -1, -1):
        if 5*i + 3*j == N:
            print(i+j)
            exit()
print(-1)