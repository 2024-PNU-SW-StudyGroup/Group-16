trial = int(input())

i = 1
j = 1
while i <= trial:
    while j <= i:
        print("*", end = "")
        j += 1
    print("")
    i += 1
    j = 1