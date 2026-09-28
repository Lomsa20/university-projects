class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Delete a node by value
    def delete(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                if temp.prev is None:  # head node
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None
                else:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next

    # Traverse forward
    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <=> ")
            temp = temp.next
        print("None")

    # Traverse backward
    def traverse_back(self):
        temp = self.head
        if not temp:
            print("None")
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" <=> ")
            temp = temp.prev
        print("None")

    # Reverse the DLL
    def reverse(self):
        current = self.head
        temp = None
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev

# ------------------- Test -------------------
dll = DLL()
dll.insert("Menu 1")
dll.insert("Menu 2")
dll.insert("Menu 3")
dll.insert("Menu 4")

print("Forward traversal:")
dll.traverse_forward()

print("Backward traversal:")
dll.traverse_back()

dll.delete("Menu 2")
print("After deleting 'Menu 2':")
dll.traverse_forward()

dll.reverse()
print("After reversing:")
dll.traverse_forward()
 