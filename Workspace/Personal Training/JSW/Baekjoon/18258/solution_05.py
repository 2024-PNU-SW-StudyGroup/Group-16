# sol 6. Array-based resizable Circular Queue 구현 => 통과
import sys

class Queue:
    def __init__(self, capacity=32):
        self.__capacity = capacity
        self.__array = [0] * capacity
        self.__front = 0
        self.__tail = 0
        self.__size = 0

    def __len__(self):
        return self.__size
    
    def __str__(self):
        return " ".join(map(str, self.__array))
    
    def enqueue(self, value):
        if self.is_full():
            self.__resize()
        self.__array[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__capacity
        self.__size += 1
        
    def dequeue(self):
        if self.is_empty():
            return -1
        
        removed = self.__array[self.__front]
        self.__front = (self.__front + 1) % self.__capacity
        self.__size -= 1
        return removed
        
    def is_empty(self):
        return self.__size == 0
    
    def is_full(self):
        return self.__size == self.__capacity
    
    def __resize(self):
        temp = [0] * (self.__capacity * 2)
        for i in range(self.__capacity):
            temp[i] = self.__array[(self.__front+i)%self.__capacity]
        self.__front = 0
        self.__tail = self.__capacity
        self.__array = temp
        self.__capacity *= 2

    def front(self):
        return -1 if self.is_empty() else self.__array[self.__front]
    
    def back(self):
        return -1 if self.is_empty() else self.__array[(self.__tail - 1) % self.__capacity]
    
queue = Queue()
N = int(sys.stdin.readline().strip('\n'))
result = []
for line in sys.stdin.read().splitlines():
    command = line.split()
    if command[0] == "push":
        queue.enqueue(int(command[1]))
    elif command[0] == "pop":
        result.append(queue.dequeue())
    elif command[0] == "size":
        result.append(len(queue))
    elif command[0] == "empty":
        result.append('1' if queue.is_empty() else '0')
    elif command[0] == "front":
        result.append(queue.front())
    elif command[0] == "back":
        result.append(queue.back())

sys.stdout.write("\n".join(map(str, result)))