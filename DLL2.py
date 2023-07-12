'''Instructions:
DLL: Reverse (⚡Interview Question)
Create a new method called reverse that reverses the order of the nodes in the list, i.e., the first node becomes the last node, the second node becomes the second-to-last node, and so on.

To do this, you'll need to traverse the list and change the direction of the pointers between the nodes so that they point in the opposite direction. Once you've done this for all nodes, you'll also need to update the head and tail pointers to reflect the new order of the nodes.'''


def reverse(self):
    temp = self.head 
    while temp :
        temp.prev, temp.next = temp.next, temp.prev 
        temp = temp.prev
        
    self.head, self.tail = self.tail, self.head  