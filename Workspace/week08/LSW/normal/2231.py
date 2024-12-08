num = int(input())
cr = 0
def creation(n):
    result = n
    while n!=0:
        result += n%10
        n //= 10
    return result

for i in range(num):
    if creation(i)==num:
        cr = i
        break
print(cr)