# Problem: 설탕 배달(https://www.acmicpc.net/problem/2839)
# Comment: 
# - 3kg 봉지의 개수를 구하는 for 루프를 제거함 -> 오히려 실행 시간이 늘어남..

N = int(input())
for i in range(N//5, -1, -1):
    if (N - 5*i)%3 == 0:
        j = (N - 5*i)//3
        print(i+j)
        exit()
print(-1)