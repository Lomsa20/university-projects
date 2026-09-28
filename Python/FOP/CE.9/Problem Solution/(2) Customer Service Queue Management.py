class PrintJob:
    def __init__(self, job_id, doc_name, num_page):
        self.job_id = job_id
        self.doc_name = doc_name
        self.num_page = num_page

    def __str__(self):
        return f"{self.job_id} | {self.doc_name} | {self.num_page} pages"
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def peek(self):
        return self.items[0] if not self.is_empty() else "Queue is empty"

    def size(self):
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Current print queue:")
            for item in self.items:
                print(item)


if __name__ == "__main__":
    # Create a queue for print jobs
    print_queue = Queue()

    # Add print jobs
    print_queue.enqueue(PrintJob(1, "Report.pdf", 10))
    print_queue.enqueue(PrintJob(2, "Homework.docx", 5))
    print_queue.enqueue(PrintJob(3, "Presentation.pptx", 20))

    print("\n--- Initial Print Queue ---")
    print_queue.display()

    print("\nNext job:", print_queue.peek())

    print("\nPrinting:", print_queue.dequeue())

    print("\n--- Queue After Printing One Job ---")
    print_queue.display()

    print("\nQueue Size:", print_queue.size())

    print("\nPrinting:", print_queue.dequeue())
    print("Printing:", print_queue.dequeue())

    print("\nIs Queue Empty?", print_queue.is_empty())
