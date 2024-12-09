left, right = map(int, input().split())
i = left

def eight_finder(num):
    eight_count = 0
    while num > 0:
        if num % 10 == 8:
            eight_count += 1
        num = num // 10
    return eight_count

def digit(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count

'''
while i <= right:
    if eight_finder(i) < score:
        score = eight_finder(i)
    i += 1
'''

diffrence = right - left
# trial = digit(diffrence) - 1

if eight_finder(left) < eight_finder(right):
    print(eight_finder(left))
else:
    print(eight_finder(right))