# Problem: 영화감독 숌(https://www.acmicpc.net/problem/1436)
# Comment: 

def is_the_end_number(n:str):
    return n.count('666')

N = int(input())
result = 0
i = 666
while N > 0:
    if is_the_end_number(str(i)):
        history = i
        N -= 1
    i += 1
print(history)