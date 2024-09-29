N = int(input())
nums = list(map(int, input().split()))
v = int(input())

result = [e for e in nums if e == v]
# result = filter(lambda x: x == v, nums)
print(len(list(result)))