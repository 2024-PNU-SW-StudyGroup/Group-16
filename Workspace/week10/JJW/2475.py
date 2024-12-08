a, b, c, d, e = map(int, input().split())

def square(num):
    return num * num

inspection_number = (square(a) + square(b) + square(c) + square(d) + square(e)) % 10
print(inspection_number)