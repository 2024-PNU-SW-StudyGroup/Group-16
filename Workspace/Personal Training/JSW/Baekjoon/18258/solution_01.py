# sol 2. LinkedList Queue => 시간 초과.

import sys

class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, None, self.head)
        self.head.next = self.tail
        self.size = 0

    def push(self, value):
        if self.head.next == self.tail:
            temp = Node(value, self.tail, self.head)
            self.head.next = temp
            self.tail.prev = temp
        else:
            temp = Node(value, self.tail, self.tail.prev)
            self.tail.prev.next = temp
            self.tail.prev = temp
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            return '-1'
        temp = self.head.next
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1
        return temp.value
    
    def empty(self):
        return '1' if self.size == 0 else '0'
    
    def front(self):
        return self.head.next.value if self.size != 0 else '-1'
    
    def back(self):
        return self.tail.prev.value if self.size != 0 else '-1'


queue = Queue()
N = int(sys.stdin.readline().strip('\n'))
result = []
for line in sys.stdin.read().splitlines():
    command = line.split()
    if command[0] == "push":
        queue.push(command[1])
    elif command[0] == "pop":
        result.append(queue.pop())
    elif command[0] == "size":
        result.append(str(queue.size))
    elif command[0] == "empty":
        result.append(queue.empty())
    elif command[0] == "front":
        result.append(queue.front())
    elif command[0] == "back":
        result.append(queue.back())

sys.stdout.write("\n".join(result))