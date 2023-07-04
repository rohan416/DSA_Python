'''Instructions:
LL: Find Kth Node From End (⚡Interview Question)
Method name:
find_kth_from_end

Find the item that is a certain number of steps away from the end of the linked list WITHOUT USING LENGTH.

For example, let's say you want to find the item that is 3 steps away from the end of the LL. To do this, you would start from the head of the LL and move through the links until you reach the item that is 3 steps away from the end.

This is the problem of finding the "kth node from the end" of a linked list. Your task is to write a program that takes as input a linked list and a number k, and returns the item that is k steps away from the end of the list. If the linked list has fewer than k items, the program should return None.'''


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
        
    #SOLUTION:
    
    def find_kth_from_end(self, k):
        slow = fast = self.head
        
        while fast:
            if fast is None:
                return None
            fast = fast.next
            
        while fast:
            slow = slow.next
            fast = fast.next
            
        return slow