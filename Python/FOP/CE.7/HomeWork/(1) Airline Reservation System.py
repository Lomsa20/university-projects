class Node:
    def __init__(self, name, status, seat_num):
        self.status = status
        self.seat_num = seat_num
        self.name = name
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert_at_end(self, name, status, seat_num):
        new_node = Node(name, status, seat_num)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        new_node.prev = temp
    def delete(self,seat_num):
        temp = self.head
        #head node is the one to delete
        if temp.seat_num and temp.seat_num.next == seat_num:
            self.head = temp.next
            return
        #search for the node to delete
        while temp and temp.seat_num != seat_num:
            prev = temp
            temp = temp.next
        #Node not found
        if not temp:
            return
        #unlink the node
        prev.next = temp.next
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.name, end=" -> ")
            temp = temp.next
        print("None")
    def display(self):
        temp = self.head
        if not temp:
            print("Empty")
            return
        while temp:
            print(temp.name, end=" -> ")
            temp = temp.next
        print("None")
sll = SLL()
sll.insert_at_end('A', 'B', 1)
sll.insert_at_end('B', 'C', 2)

sll.display()   # 10 -> 20 -> 30 -> None
