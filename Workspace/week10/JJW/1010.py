number_of_cases = int(input())

i = 0
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return factorial(num - 1) * num

def combination(a, b):
    numerator = factorial(b)
    denominator = factorial(a) * factorial(b - a)
    return int(numerator / denominator)


while i < number_of_cases:
    temp_a, temp_b = map(int, input().split())
    print(combination(temp_a, temp_b))
    i += 1