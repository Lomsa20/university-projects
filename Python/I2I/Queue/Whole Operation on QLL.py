class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, x):
        new_node = Node(x)
        if self.isEmpty():
            self.front == None, self.rear == None
        else:

            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            self.front = self.rear == None
            return "underflow"
        else:
            temp = self.front
            self.front = self.front.next
            if self.front == None:
                self.rear = None

    def getfront(self):
        if self.isEmpty():
            return -1
        return self.front.data
    def getrear(self):
        if self.isEmpty():
            return -1
        return self.rear.data

