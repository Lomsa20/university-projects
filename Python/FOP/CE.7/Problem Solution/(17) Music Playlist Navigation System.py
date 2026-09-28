class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DLL:
    def __init__(self):
        self.head = None
    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    def delete(self,data):
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
            print(temp.data, end=' <=> ')
            temp = temp.next
        return None
    def traverse_back(self):
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=' <=> ')
            temp = temp.prev
        return None
dll = DLL()

dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_end(40)

print("Forward traversal:")
dll.traverse_forward()
print()

print("Backward traversal:")
dll.traverse_back()
print()

dll.delete(20)

print("After deleting 20 (forward):")
dll.traverse_forward()
print()

print("After deleting 20 (backward):")
dll.traverse_back()
print()
