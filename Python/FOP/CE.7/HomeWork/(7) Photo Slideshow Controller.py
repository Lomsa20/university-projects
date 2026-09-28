class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
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

        while temp:
            if temp.data == data:
                # deleting head
                if temp.prev is None:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None
                else:
                    temp.prev.next = temp.next

                # deleting middle or tail
                if temp.next:
                    temp.next.prev = temp.prev
                return

            temp = temp.next

    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <=> ")
            temp = temp.next
        print("None")

    def traverse_back(self):
        temp = self.head
        if not temp:
            print("None")
            return

        # go to last node
        while temp.next:
            temp = temp.next

        # traverse backward
        while temp:
            print(temp.data, end=" <=> ")
            temp = temp.prev
        print("None")
dll = DLL()
dll.insert("Photo1")
dll.insert("Photo2")
dll.insert("Photo3")
dll.insert("Photo4")

dll.traverse_forward()
dll.traverse_back()

dll.deletion("Photo2")
dll.traverse_forward()

dll.deletion("Photo1")
dll.traverse_forward()

dll.deletion("Photo4")
dll.traverse_forward()
