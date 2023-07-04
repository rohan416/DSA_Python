# Write a method to find and return the middle node in the Linked List WITHOUT using the length attribute.

def find_middle_node(self):
    slow =slow.head
    fast =fast.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
