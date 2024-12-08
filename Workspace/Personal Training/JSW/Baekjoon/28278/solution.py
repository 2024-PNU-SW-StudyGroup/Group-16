class Node:
 def __init__(self, data, next):
  self.data = data
  self.next = next
class stack:
 def __init__(self):
  self.top = Node(None, None)
  self.size = 0

 def push(self, x):
  temp = Node(x, self.top)
  self.top = temp
  self.size += 1

 def pop(self):
  if self.is_empty():
   return -1
  temp = self.top.data
  self.top = self.top.next
  self.size -= 1
  return temp
 
 def peek(self):
  if self.is_empty():
   return -1
  return self.top.data
 
 def __len__(self):
  return self.size
 
 def is_empty(self):
  return self.size == 0
  


stack  = stack()
N = int(input())
output = []
for i in range(N):
 line = input().split()
 if line[0] == '1':
  stack.push(int(line[1]))
 elif line[0] == '2':
  output.append(stack.pop())
 elif line[0] == '3':
  output.append(len(stack))
 elif line[0] == '4':
  output.append(1 if stack.is_empty() else 0)
 else:
  output.append(stack.peek())

print(*output, sep='\n')