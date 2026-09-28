class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_lists(a, b):
    dummy = Node(0)
    tail = dummy

    while a and b:
        if a.data < b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    tail.next = a or b
    return dummy.next


def sort_list(head):
    if not head or not head.next:
        return head

    # Find middle
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None  # split

    left = sort_list(head)
    right = sort_list(mid)

    return merge_lists(left, right)


def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")
# Build unsorted list: 4 -> 2 -> 1 -> 3
n1 = Node(4)
n2 = Node(2)
n3 = Node(1)
n4 = Node(3)

n1.next = n2
n2.next = n3
n3.next = n4

print("Before sorting:")
print_list(n1)

sorted_head = sort_list(n1)

print("After sorting:")
print_list(sorted_head)
