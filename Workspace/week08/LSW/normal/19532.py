nums = list(map(int, input().split()))
a, b, c, d, e, f = nums
y = (a * f - c * d) // (a * e - b * d)
x = (c * e - b * f) // (a * e - b * d)

print(x, y)