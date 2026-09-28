class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Customer_Queue:
    def __init__(self):
        self.head = None
    def enqueue_vip(self, customer):
        newnode = Node(customer)
        newnode.next = self.head
        self.head = newnode
    def enqueue_regular(self, customer):
        newnode = Node(customer)
        if not self.head:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end = " -> ")
            temp = temp.next
        print("null")
queue = Customer_Queue()
queue.enqueue_regular('Alice')
queue.enqueue_vip('VIP Bob')
queue.enqueue_regular('Charlie')
queue.display()
