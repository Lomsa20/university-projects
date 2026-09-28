class Node:
    def __init__(self,post, timestamp):
        self.post = post
        self.timestamp = timestamp
        self.next = None
class Feed:
    def __init__(self):
        self.head = None
    def add_post(self,post):
        new_node = Node('',None)
        new_node.next = self.head
        self.head = new_node
    def remove_duplicates(self):
        seen = set()
        temp = self.head
        prev = None
        while temp:
            if temp.post in seen:
                prev.next = temp.next
            else:
                seen.add(temp.post)
                prev = temp
            temp = temp.next
    def sort_by_timestamp(self):
        self.head = self.merge_sort(self.head)
    def merge_sort(self,head):
        if not head or head.next:
            return head
        mid = self.get_mid(head)
        left = head
        right = mid.next
        return self.merge(self.merge_sort(left), self.merge_sort(right))
    def get_mid(self,head):
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, a, b):
        dummy = Node('',0)
        tail = dummy
        while a and b:
            if a.timestamp > b.timestamp:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail.next = a or b
            return dummy.next
    def show_feed(self):
        posts = []
        temp = self.head
        while temp:
            posts.append(temp.post)
            temp = temp.next
        return posts
