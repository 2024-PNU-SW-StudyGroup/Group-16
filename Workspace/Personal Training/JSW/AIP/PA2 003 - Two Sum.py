def two_sum(numbers, target):
    temp = 0
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j] == target:
                return (i, j), (numbers[i], numbers[j])
                
    return [(None), (None)]

numbers = list(map(int, input().split()))
target = int(input())

indexs, values = two_sum(numbers, target)
print(f"indexes: {indexs}, values: {values}")