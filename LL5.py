'''Instructions:
LL: Reverse Between (⚡Interview Question)
You are given a singly linked list and two integers m and n. Your task is to write a method reverse_between within the LinkedList class that reverses the nodes of the linked list from index m to index n (inclusive) in one pass and in-place.

Input

The method reverse_between takes two integer inputs m and n.

The method will only be passed valid indexes (you do not need to test whether the indexes are out of bounds)'''


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
        
    def reverse_mn(self, m,n):
        if self.head is None:
            return None
            
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        
        for _ in range(m):
            prev = prev.next
         
        current = prev.next
        for _ in range(m-n):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next =temp
        self.head = dummy.next
            
        
