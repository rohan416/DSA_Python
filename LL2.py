'''Instructions:
LL: Has Loop (⚡Interview Question)
Write a method called has_loop that is part of the linked list class.

The method should be able to detect if there is a cycle or loop present in the linked list.

The method should utilize Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm, to determine the presence of a loop efficiently.

The method should follow these guidelines:



Create two pointers, slow and fast, both initially pointing to the head of the linked list.

Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.

If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this occurs, the method should return True.

If the fast pointer reaches the end of the list or encounters a None value, it means there is no loop in the list. In this case, the method should return False.'''

#SOLUTION :
class Node:
    def __init__(self,value):
        self.value =value
        self.next= None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def has_loop(self):
        tortoise = self.head
        hare = self.head

        while hare is not None and hare.next is not None:
            tortoise = tortoise.next  # Move tortoise one step
            hare = hare.next.next  # Move hare two steps

            if tortoise == hare:
                return True  # Cycle detected

        return False