n = int(input())
for i in range(1,n+1):
    if i%3 == 0 and i%5 == 0:
        print(i)
        i += 1