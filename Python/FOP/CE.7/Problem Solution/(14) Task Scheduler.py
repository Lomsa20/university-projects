class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Scheduler:
    def __init__(self):
        self.head = None
    def add_task(self, task):
        new_node = Node(task)
        if not self.head:
           self.head= new_node
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def rotate(self):
        if not self.head or not self.head.next:
            return
        first = self.head
        self.head = self.head.next
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = first
        first.next = None

    def remove_task(self, task):
        temp = self.head
        prev = None
        while temp:
            if temp.data == task:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return
            prev = temp
            temp = temp.next
    def show_tasks(self):
        tasks = []
        temp = self.head
        while temp:
            tasks.append(temp.data)
            temp = temp.next
        return tasks