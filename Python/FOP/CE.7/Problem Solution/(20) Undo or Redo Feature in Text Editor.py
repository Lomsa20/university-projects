class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DLL:
    def __init__(self):
        self.head = None
    def insert_end(self,data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        
    def delete(self, data):
        temp =self.head
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
            print(temp.data,end=" -> ")
            temp = temp.next
        print('None')
    
    def traverse_backward(self):
        temp =self.head
        while temp:
            temp = temp.prev
        while temp:    
            print(temp.data,end=" <-> ")
            temp = temp.next
        print("None")