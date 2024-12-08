temp_a = 1
temp_b = 1
while True:
    temp_a, temp_b = map(int, input().split())
    if temp_a == 0 and temp_b == 0:
        break
    else:
        print(temp_a + temp_b)