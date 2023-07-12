'''Instructions:
DLL: Swap Nodes in Pairs (⚡Interview Question)
You are given a doubly linked list.

Implement a method called swap_pairs within the class that swaps the values of adjacent nodes in the linked list. The method should not take any input parameters.

Note: This DoublyLinkedList does not have a tail pointer which will make the implementation easier.

Example:

1-->2-->3-->4--> should become 2-->1-->4-->3-->

Your implementation should handle edge cases such as an empty linked list or a linked list with only one node.

Note: You must solve the problem without modifying the values in the list's nodes (i.e., only the nodes' prev and next pointers may be changed.)
'''

def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
 
        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next
 
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
 
            second_node.prev = prev
            first_node.prev = second_node
            if first_node.next:
                first_node.next.prev = first_node
 
            self.head = first_node.next
            prev = first_node
 
        self.head = dummy.next