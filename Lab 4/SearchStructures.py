"""
name: Joe Le
ENGR 221 Lab 4
"""

# Implementation of a Stack
class Stack():
    def __init__(self):
        self.items = []

    # Returns True if the Stack is empty, or False if it is not empty
    def isEmpty(self):
        return len(self.items) == 0
        

    # For a Stack, this should "push" item to the top of the Stack
    def add(self, item):
        self.items.append(item) #push

    # For a Stack, this should "pop" an item from the Stack
    # and return it
    def remove(self):
        return self.items.pop() #pop, LIFO
    
# Implementation of a Queue
class Queue():
    def __init__(self):
        self.items = []

    # Returns True if the Queue is empty, or False if it is not empty
    def isEmpty(self):
        return len(self.items) == 0 

    # For a Queue, this should "enqueue" item to the end of the Queue
    def add(self, item):
        return self.items.append(item) #enqueue

    # For a Queue, this should "dequeue" an item from the Queue
    # and return it
    def remove(self):
        return self.items.pop(0) #dequeue, FIFO
    
    