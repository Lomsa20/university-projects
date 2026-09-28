class Node:
    def __init__(self, val):
        self.val = val
        self.prev= None
        self.next = None
class MiddleStack:
    def __init__(self):
        self.head = None
        self.count = 0
        self.mid = None
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        if self.head is None:
            self.head.prev = new_node
        self.head = new_node
        self.count += 1
        if self.count == 1:
            self.mid = new_node
        elif self.count %2 == 0:
            self.mid = self.mid.prev
    def pop(self):
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.count -= 1
        if self.count % 2 == 1 and self.mid:
            self.mid = self.mid.next
        return val
    def find_mid(self):
        return self.mid.val if self.mid else None
    def delete_mid(self):
        if not self.mid: return None
        if self.mid.prev:
            self.mid.prev.next = self.next
        if self.mid.next:
            self.mid.next.prev = self.prev
        if self.count % 2 == 0:
            self.mid = self.mid.next
        else:
            self.mid = self.mid.prev
        self.count -= 1
        return val