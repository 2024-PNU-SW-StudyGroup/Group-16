# sol 5. eval 사용 => 시간 초과

from collections import *
import sys

queue = deque()
push = lambda x: queue.append(x)
pop = lambda: queue.popleft() if queue else -1
size = lambda: len(queue)
empty = lambda: 1 if not queue else 0
front = lambda: queue[0] if queue else -1
back = lambda: queue[-1] if queue else -1

N = int(sys.stdin.readline().strip('\n'))
output = []
for _ in range(N):
    line = sys.stdin.readline().strip('\n').split()
    if line[0] == "push":
        command = f"{line[0]}({line[1]})"
        eval(command)
    else:
        command = f"{line[0]}()"
        output.append(eval(command))
sys.stdout.write("\n".join(map(str, output)))