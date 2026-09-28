class MyQueue:
    def __init__(self, capacity):
        # max num can hold
        self.capacity = capacity
        # array to store queue
        self.arr = [0] * capacity
        # current num of element
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def enqueue(self, x):
        if self.size is self.capacity:
            print("overflow")
            return
        self.arr[self.size] = x
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("underflow")
            return
        for i in range(1, self.size):
            self.arr[i - 1] = self.arr[i]
        self.size -= 1

    def getfront(self):
        if self.size == 0:
            return -1
        return self.arr[0]

    def rear(self):
        if self.isEmpty:
            return -1
        return self.arr[self.size - 1]


if __name__  == '__main__':
    q = MyQueue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print("front",q.getfront())
    print("rear",q.rear())
    print("size",q.size)
    print("enqueue",q.enqueue(6))
    print("isFull",q.isFull())
    print("isEmpty",q.isEmpty())