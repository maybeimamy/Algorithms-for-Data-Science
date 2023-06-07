
## Amy Schneider, COMP 4581, Lab 5 ##

from collections import deque

class MyStack:

    # create it - " use a standard Python list"
    def __init__(self, num):
        self.num = num
        self.stack = []

    # add to it
    def push(self, value):
        self.stack.append(value)

    # remove from it
    def pop(self):
        return self.stack.pop()

    # peek at the top/front element
    def top(self):
        return self.stack[0]

    # determine if stack is empty (return True if empty, False if not)
    def empty(self):
        if len(self.stack) == 0:
            return True
        return False

class MyQueue:

    # create it - "use a Python deque"
    def __init__(self, num):
        self.num = num
        self.queue = deque()

    # add to it (from back)
    def enqueue(self, value):
        self.queue.append(value)

    # remove from it (from front)
    def dequeue(self):
        return self.queue.popleft()

    # peek at the top/front element
    def front(self):
        return self.queue[0]

    # determine if queue is empty (return True if empty, False if not)
    def empty(self):
        if len(self.queue) == 0:
            return True
        return False

# Testing code for stack

s = MyStack(int)
print(s.empty())
# Output - True
s.push(5)
s.push(8)
print(s.pop())
# Output - 8
s.push(3)
print(s.empty())
# Output - False
print(s.top())
# Output - 5
print(s.pop())
# Output - 3
print(s.pop())
# Output - 5
print(s.pop())  # should generate an error
# Output - IndexError: pop from empty list

# Testing code for Queue

q = MyQueue(int)
print(q.empty())
# Output - True
q.enqueue(5)
q.enqueue(8)
print(q.dequeue())
# Output - 5
q.enqueue(3)
print(q.empty())
# Output - False
print(q.front())
# Output - 8
print(q.dequeue())
# Output - 8
print(q.dequeue())
# Output - 3
print(q.dequeue())  # should generate an error
# Output - IndexError: pop from an empty deque
