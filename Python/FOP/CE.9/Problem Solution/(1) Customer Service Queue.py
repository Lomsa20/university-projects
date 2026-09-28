class Customer:
    def __init__(self,customer_id,name,email ):
        self.customer_id = customer_id
        self.name = name
        self.email = email
    def __str__(self):
        return f"{self.customer_id}, {self.name}, {self.email}"
    def update_details(self, name=None, email=None):
        if name:
            self.name = name
        if email:
            self.email = email
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)
    def is_empty(self):
        return len(self.items) == 0
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "queue is empty"
    def peek(self):
        return self.items[0] if not self.is_empty() else ("queue is empty")
    def size(self):
        return len(self.items)
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Current Queue is")
            for item in self.items:
                print(item)
    def search(self,customer_id):
        for customer in self.items:
            if customer_id == customer.customer_id:
                return customer
            return None
    def export_to_list(self):
        return [customer for customer in self.items]
if __name__ == "__main__":
 queue = Queue()
 # Add customers
 queue.enqueue(Customer(101, "Alice", "alice@example.com"))
 queue.enqueue(Customer(102, "Bob", "bob@example.com"))
 queue.enqueue(Customer(103, "Charlie",
"charlie@example.com"))
 print("\nDisplay Queue:")
 queue.display()
 print("\nNext to be served:", queue.peek())
 print("\nServing:", queue.dequeue())
 queue.display()
 print("\nSearch for Customer ID 102:")
 customer = queue.search(102)
 print(customer if customer else "Customer not found")
 print("\nUpdate Customer ID 102:")
 if customer:
     customer.update_details(name="Bob Smith",
                             email="bobsmith@example.com")
 queue.display()
 print("\nExport to List:")
 for c in queue.export_to_list():
     print(c)
 print("\nQueue Size:", queue.size())