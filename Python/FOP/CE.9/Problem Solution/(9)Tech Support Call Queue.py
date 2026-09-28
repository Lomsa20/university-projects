class SupportCall:
    def __init__(self, call_id,name,issue):
        self.call_id = call_id
        self.name = name
        self.issue = issue
    def __str__(self):
        return f'Call: {self.call_id}, Name: {self.name}, Issue: {self.issue}'
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        return self.items.append(item)
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return "Queue is Empty"
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[0] if self.isEmpty() else "queue is empty"
    def display(self,item):
        if self.isEmpty():
          return "Queue is Empty"
        else:
            print("Tech Support Call Queue:")
            for item in self.items:
                print(item)
if __name__ == "__main__":
 call_queue = Queue()
 call_queue.enqueue(SupportCall(901, "Alice", "Internet notworking"))
 call_queue.enqueue(SupportCall(902, "Bob", "Software installationissue"))
 call_queue.enqueue(SupportCall(903, "Charlie", "Password reset"))
 print("\n--- Initial Call Queue ---")
 call_queue.display(1)
 print("\nNext Call:", call_queue.peek())
 print("\nServing:", call_queue.dequeue())
 call_queue.display(1)
 print("\nQueue Size:", call_queue.size())