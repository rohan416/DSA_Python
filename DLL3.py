'''Instructions:
DLL: Palindrome Checker (⚡Interview Question)
Write a method to determine whether a given doubly linked list reads the same forwards and backwards.

For example, if the list contains the values [1, 2, 3, 2, 1], then the method should return True, since the list is a palindrome.

If the list contains the values [1, 2, 3, 4, 5], then the method should return False, since the list is not a palindrome.'''

def is_palindrome(self):
    if self.length <= 1:
        return True
    
    for_node = self.head
    back_node = self.tail
    for _ in range(self.length//2):
        if for_node.value != back_node.value:
            return False
        for_node = for_node.next 
        back_node = back_node.prev 
    
    return True