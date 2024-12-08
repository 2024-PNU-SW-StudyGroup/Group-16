number_of_cases = int(input())

i = 0
for i in range(0, number_of_cases):
    temp_a, temp_b = map(int, input().split())
    print(temp_a + temp_b)