class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MergeStack:
    def __init__(self):
        self.head = None
        self.tail = None
    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    def merge(self, other):
        if not other.head:
            return
        other.tail.next = self.tail
        self.head = other.head
    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end = ' <=> ')
            temp = temp.next
        return "None"    