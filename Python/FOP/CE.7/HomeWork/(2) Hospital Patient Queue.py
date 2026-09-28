class Node:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.next = None

class HospitalQueue:
    def __init__(self):
        self.head = None

    def add_patient(self, name, priority):
        """Insert patient by priority (higher number = higher priority)"""
        new_node = Node(name, priority)
        # Insert at head if empty or higher priority than current head
        if not self.head or priority > self.head.priority:
            new_node.next = self.head
            self.head = new_node
            return
        # Traverse to find correct position
        current = self.head
        while current.next and current.next.priority >= priority:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def remove_patient(self, name=None):
        """
        Remove patient.
        If name is None: remove the highest priority patient (head).
        If name is provided: remove the first patient matching that name.
        """
        if not self.head:
            print("Queue is empty")
            return None

        # Remove head if no name given or head matches name
        if name is None or self.head.name == name:
            removed = self.head
            self.head = self.head.next
            removed.next = None
            return removed.name

        # Traverse to find patient by name
        prev = self.head
        current = self.head.next
        while current:
            if current.name == name:
                prev.next = current.next
                current.next = None
                return current.name
            prev = current
            current = current.next

        print(f"Patient '{name}' not found")
        return None

    def display_queue(self):
        """Display patients in queue with priorities"""
        if not self.head:
            print("Queue is empty")
            return
        temp = self.head
        while temp:
            print(f"{temp.name}(Priority: {temp.priority})", end=' <=> ' if temp.next else '')
            temp = temp.next
        print()

# -------------------------
# Example usage
hq = HospitalQueue()

# Add patients
hq.add_patient("Alice", 2)
hq.add_patient("Bob", 5)
hq.add_patient("Charlie", 3)
hq.add_patient("Diana", 4)

print("Queue after adding patients:")
hq.display_queue()

# Remove highest priority patient
treated = hq.remove_patient()
print(f"\nTreated patient: {treated}")

print("\nQueue after treating one patient:")
hq.display_queue()

# Remove a specific patient by name
removed = hq.remove_patient("Charlie")
print(f"\nRemoved patient by name: {removed}")

print("\nQueue after removing Charlie:")
hq.display_queue()

# Add another patient with high priority
hq.add_patient("Eve", 6)
print("\nQueue after adding Eve with high priority:"
