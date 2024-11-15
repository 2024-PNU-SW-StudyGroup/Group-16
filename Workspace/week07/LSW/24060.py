n, k = map(int, input().split())
array1 = [int(i) for i in input().split()]
count = 0
current_num = 0

def merge_sort(A, p, r):
    global count, current_num
    count += 1
    
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q) 
        merge_sort(A, q + 1, r)  
        merge(A, p, q, r)
    else:
        current_num = A[0]
        
    

def merge(A, p, q, r):
    global count, current_num
    tmp = [0] * (r - p + 1)
    i, j, t = p, q + 1, 0

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1

    while i <= q:
        tmp[t] = A[i]
        i += 1
        t += 1

    while j <= r:
        tmp[t] = A[j]
        j += 1
        t += 1

    for i in range(p, r + 1):
        A[i] = tmp[i - p]
        
    count += 1


merge_sort(array1, 0, len(array1)-1)    
print(count)
