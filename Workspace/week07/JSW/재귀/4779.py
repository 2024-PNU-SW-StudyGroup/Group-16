import sys
def cantor_set(set):
    if set == '-': return set
    return cantor_set(set[:len(set)//3]) + ' '*(len(set)//3) + cantor_set(set[len(set)//3*2:])


while (line := sys.stdin.readline()) != '':
    N = int(line)
    print(cantor_set('-'*(3**N)))