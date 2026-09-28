class Booking:
    def __init__(self, book_id, customer_name, num_tick):
        self.book_id = book_id
        self.customer_name = customer_name
        self.num_tick = num_tick

    def __str__(self):
        return f'{self.book_id} {self.customer_name} {self.num_tick}'


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return "Queue is empty"

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        return "Queue is empty"

    def display(self):   # FIXED
        if self.isEmpty():
            print("Queue is empty")
            return

        print("Booking Queue: ")
        for item in self.items:
            print(item)


if __name__ == "__main__":
    booking_queue = Queue()

    booking_queue.enqueue(Booking(501, "Alice", 2))
    booking_queue.enqueue(Booking(502, "Bob", 4))
    booking_queue.enqueue(Booking(503, "Charlie", 1))

    print("\n--- Initial Booking Queue ---")
    booking_queue.display()

    print("\nNext Booking:", booking_queue.peek())

    print("\nProcessing:", booking_queue.dequeue())

    print("\n--- After Processing ---")
    booking_queue.display()

    print("\nQueue Size:", booking_queue.size())
