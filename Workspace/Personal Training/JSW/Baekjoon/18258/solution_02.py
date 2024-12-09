# sol 3. deque 모듈 사용 => 통과

from collections import deque
import sys

queue = deque()
N = int(sys.stdin.readline().strip('\n'))
result = []
for line in sys.stdin.read().splitlines():
    command = line.split()
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        result.append(queue.popleft() if queue else '-1')
    elif command[0] == "size":
        result.append(str(len(queue)))
    elif command[0] == "empty":
        result.append('1' if len(queue) == 0 else '0')
    elif command[0] == "front":
        result.append(queue[0] if queue else '-1')
    elif command[0] == "back":
        result.append(queue[-1] if queue else '-1')

sys.stdout.write("\n".join(result))