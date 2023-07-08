'''You need to implement this method as a method of the LinkedList class. The method should take an integer x as input. If the linked list is empty, the method should return None.

To implement this method, you should create two new linked lists. These two linked lists will be made up of the original nodes from the linked list that is being partitioned, one for nodes less than x and one for nodes greater than or equal to x.  None of the nodes from the linked list should be duplicated.

The creation of a limited number of new nodes is allowed (e.g., dummy nodes to facilitate the partitioning process).

You should then traverse the original linked list and append each node to the appropriate new linked list.

Finally, you should connect the two new linked lists together.'''


def Partition(self,x):
    if not self.head:
        return None
        
    dum1 = Node(0)
    dum2 = Node(0)
    prev1 = dum1
    prev2 = dum2
    current = self.head
    
    while current:
        if current.value < x:
            prev1.next = current
            prev1 = current
        else:
            prev2.next = current
            prev2 = current
    
        current = current.next
        
    prev2.next = None
    prev1.next = dum2.next
    
    self.head = dum1.next
    
