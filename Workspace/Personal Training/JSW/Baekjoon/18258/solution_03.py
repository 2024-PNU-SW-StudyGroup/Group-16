# sol 4. pop() 사기치기 => 통과

import sys

class Queue:
    def __init__(self):
        self.arr = []
        self.idx = 0
    
    def push(self, value):
        self.arr.append(value)

    def empty(self):
        return 1 if self.size() == 0 else 0
    
    def pop(self):
        if self.empty():
            return -1
        temp = self.arr[self.idx]
        self.idx += 1
        return temp
    
    def size(self):
        return len(self.arr) - self.idx
    
    def front(self):
        if self.empty():
            return -1
        return self.arr[self.idx]

    def back(self):
        if self.empty():
            return -1
        return self.arr[-1]

        
queue = Queue()

N = int(sys.stdin.readline())
result = []
for line in sys.stdin.read().splitlines():
    line = line.split()
    if line[0] == "push":
        queue.push(line[1])
    elif line[0] == "pop":
        result.append(queue.pop())
    elif line[0] == "size":
        result.append(queue.size())
    elif line[0] == "empty":
        result.append(queue.empty())
    elif line[0] == "front":
        result.append(queue.front())
    elif line[0] == "back":
        result.append(queue.back())

sys.stdout.write("\n".join(map(str, result)))
