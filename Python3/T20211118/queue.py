# -*-coding: utf-8 -*-
# 队列


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


a_queue = Queue()
print(a_queue.is_empty())
for i in range(5):
    a_queue.enqueue(i)

print(a_queue.size())

print()
for i in range(a_queue.size()):
    print(a_queue.dequeue())

print("size:" + str(a_queue.size()))
