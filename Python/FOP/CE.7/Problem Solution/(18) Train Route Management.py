class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DLL:
    def __init__(self):
        self.head = None
    def insertion_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    def delete_train(self,data):
        temp = self.head
        while temp:
            if temp.data == data:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                return
            temp = temp.next
    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data,end=' <=> ')
            temp = temp.next
        print('None')
    def traverse_back(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data,end=' <=> ')
            temp = temp.prev
        print('None')
dll = DLL()
dll.insertion_end(1)
dll.insertion_end(2)
dll.insertion_end(3)

print("Forward:")
dll.traverse_forward()

print("\nBackward:")
dll.traverse_back()
