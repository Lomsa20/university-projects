class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DLL:
    def __init__(self):
        self.head = None
    def insertion_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    def deletion(self, data):
        temp = self.head
        while temp.next:
            if temp.next.data == data:
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
            print(temp.data, end=" <=> ")
            temp = temp.next
        return "None"
    def traverse_back(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" <=> ")
            temp = temp.prev
        return "None"
dll = DLL()
dll.insertion_end(1)
dll.insertion_end(2)
dll.insertion_end(3)

print("Forward:")
dll.traverse_forward()

print("\nBackward:")
dll.traverse_back()
