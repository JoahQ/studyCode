# -*-coding: utf-8 -*-
# 栈

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
print(stack.is_empty())
print(stack.peek())
print(stack.size())
print("-="*12)
sk = Stack()
for i in range(0, 6):
    sk.push(i)
print(sk.peek())
print(sk.size())
print("-")
sk.pop()
print(sk.peek())
print(sk.size())
print("=="*15)
stack1 = Stack()
for c in "Hello, world!":
    stack1.push(c)

reverse = ''

for i in range(stack1.size()):
    reverse += stack1.pop()

print(reverse)
