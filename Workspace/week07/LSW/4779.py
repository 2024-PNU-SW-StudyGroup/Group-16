import sys
n_input = []

for line in sys.stdin:
    n_input.append(int(line.strip()))


def add_element(n): 
    if n==0:
        return [0]
    else:
        return add_element(n-1) + [n] + add_element(n-1)

def cantor(n):
    element_list = add_element(n) 
    n_list = [0] * (3 ** n)
    n_list[0] = 1
    c = 0
    i = 0
    while n_list[-1]==0 :
        
        i += 3**element_list[c] + 1
        n_list[i] = 1
        c += 1

        
    for _ in range(len(n_list)):
        if n_list[_]:
            print("-", end="")
        else:
            print(" ",end="")

for j in range(len(n_input)):
    cantor(n_input[j])
    print("")