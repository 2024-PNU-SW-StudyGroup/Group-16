n = int(input())

def recursive_fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return recursive_fibo(n-1)+recursive_fibo(n-2)

print(recursive_fibo(n))