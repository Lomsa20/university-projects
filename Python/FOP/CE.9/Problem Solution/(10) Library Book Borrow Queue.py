class Library:
    def __init__(self, r_id, name, title):
        self.r_id =r_id
        self.name = name
        self.title = title
    def __str__(self):
        return f"{self.r_id},{self.name},{self.title}"
class Queue:
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def enqueue(self,item):
        return self.items.append(item)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return"queue is empty"
    
    def peek(self):
        return self.items[0] if not self.isEmpty else "Queue is empty"
    
    def display(self,item):
        if self.isEmpty():
            print("queue is empty")
        else:
            print("borrow request")
            for item in self.items:
                print(item)
if __name__ == "__main__":
 borrow_queue = Queue()
 borrow_queue.enqueue(BorrowRequest(1001, "Alice", "PythonProgramming"))
 borrow_queue.enqueue(BorrowRequest(1002, "Bob", "DataStructures"))
 borrow_queue.enqueue(BorrowRequest(1003, "Charlie", "MachineLearning"))
 print("\n--- Initial Borrow Queue ---")
 borrow_queue.display(1)
 print("\nNext Request:", borrow_queue.peek())
 print("\nProcessing:", borrow_queue.dequeue())
 borrow_queue.display(1)
 print("\nQueue Size:", borrow_queue.size())
    