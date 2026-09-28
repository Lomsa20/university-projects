class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def merge_list(l1, l2):
    dummy = Node(0) #this is fake head that simplifies edge cases(empty list, first insert)
    tail = dummy #always point last node
    while l1 and l2: #as long as both lists have nodes keep merging
        if l1.data < l2.data: #this pick smaller value, attach it to the merged list
            tail.next = l1 #move forward in the list you took from
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next # we aren't create new node ,just rewriting pointers
        tail = tail.next # move tail
    tail.next = l1 or l2 # attach leftover
    return dummy.next # return real head