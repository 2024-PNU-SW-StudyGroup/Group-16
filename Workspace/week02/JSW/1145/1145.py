def GCD(a:int, b:int)->int:
    if a < b:
        return GCD(b, a)
    if b == 0:
        return a
    return GCD(b, a%b)

def LCM(a:int, b:int)->int:
    return int(a*b/GCD(a,b))

def LCM_list(args:list)->int:
    result = args[0]
    for i in range(1, len(args)):
        result = LCM(result, args[i])
    return result

nums = list(map(int, input().split()))
result = nums[0]*nums[1]*nums[2]
for i in range(0, 5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            result = min(result, LCM_list([nums[i], nums[j], nums[k]]))

print(result)