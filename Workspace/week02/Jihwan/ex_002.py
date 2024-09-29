def jegui(n):
    if n>0:
        jegui(n-1)
    print(n)

jegui(20)