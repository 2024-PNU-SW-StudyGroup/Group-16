N, X = map(int, input().split())
result_list = list(map(int ,input().split()))

i = 0

for i in range(0, N):
    if result_list[i] < X:
        print(result_list[i], end = " ")