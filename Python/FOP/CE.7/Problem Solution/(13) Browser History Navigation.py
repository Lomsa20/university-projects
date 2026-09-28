class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class BrowsingHistory:
    def __init__(self):
        self.head = None
        self.current = None
    def visit(self, url):
        newnode = Node(url)
        if not self.head:
            self.head = newnode
        else:
            self.current.next = newnode
        self.current = newnode
    def back(self):
        if self.head == self.current:
            return None
        temp = self.head
        while temp.next != self.current:
            temp = temp.next
        self.current = temp
        return self.current.data
    def forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.data
        return None
    def show_history(self):
        temp = self.head
        history = []
        while temp:
            history.append(temp.data)
            temp = temp.next
        return history
history = BrowsingHistory()
history.visit("google.com")
history.visit("github.com")
history.visit("steam.com")
print(history.show_history())
print("back",history.back())
print("forward",history.forward())