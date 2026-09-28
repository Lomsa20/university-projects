class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SLinkedList:
    def __init__(self):
        self.head = None
    def Insertion_at_position(self, data,pos):
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(pos - 1):
            if temp is None:
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
    def delete_by_value(self, value):
        temp = self.head
        if temp and temp.data == value:
            self.head = temp.next
            return
        prev = None
        while temp and temp.next != value:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next
    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
train = SLinkedList()
train.Insertion_at_position("Engine",0)
train.Insertion_at_position("Carriage1",1)
train.Insertion_at_position("Carriage2",2)

print("before Reverse")
train.display()
print("after Reverse")
train.reverse()
train.display()