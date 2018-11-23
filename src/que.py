from node import Node

class Queue(object):
    def __init__(self, data=None):
        self.front = None
        self.rear = None
        self.size = 0

    def enQueue(self, data):
        self.lastNode = self.front
        self.front = Node(data, self.front)
        if self.lastNode:
            self.lastNode.setLast(self.front)
        if self.rear is None:
            self.rear = self.front
        self.size += 1

    def queueRear(self):
        if self.rear is None:
            print("Sorry, the queue is empty!")
            raise IndexError
        return self.rear.get_data()

    def queueFront(self):
        if self.front is None:
            print("Sorry, the queue is empty!")
            raise IndexError
        return self.front.get_data()

    def deQueue(self):
        if self.rear is None:
            print("Sorry, the queue is empty!")
            raise IndexError
        result = self.rear.get_data()
        self.rear = self.rear.last
        self.size -= 1
        return result
    
    def size(self):
        return self.size

    def isEmpty(self):
        return self.size==0
