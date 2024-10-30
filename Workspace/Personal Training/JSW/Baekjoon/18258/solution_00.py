# sol 1. List 사용 => 시간 초과

import sys

queue = []
push = lambda x: queue.append(x)
pop = lambda: queue.pop(0) if queue else -1
size = lambda: len(queue) 
empty = lambda: 0 if queue else 1
front = lambda: queue[0] if queue else -1
back = lambda: queue[-1] if queue else -1

N = int(sys.stdin.readline().strip('\n'))
result = []
for _ in range(N):
    line = sys.stdin.readline().strip('\n').split(' ')
    if line[0] == "push":
        push(line[1])
    elif line[0] == "pop":
        result.append(pop())
    elif line[0] == "size":
        result.append(size())
    elif line[0] == "empty":
        result.append(empty())
    elif line[0] == "front":
        result.append(front())
    elif line[0] == "back":
        result.append(back())

print(*result, sep='\n')
