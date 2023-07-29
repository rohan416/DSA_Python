'''HT: Group Anagrams (⚡Interview Question)
You have been given an array of strings, where each string may contain only lowercase English letters. You need to write a function group_anagrams(strings) that groups the anagrams in the array together using a hash table (dictionary). The function should return a list of lists, where each inner list contains a group of anagrams.

For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"], the function should return [["eat","tea","ate"],["tan","nat"],["bat"]] because the first three strings are anagrams of each other, the next two strings are anagrams of each other, and the last string has no anagrams in the input array.

You need to implement the group_anagrams(strings) function and return a list of lists, where each inner list contains a group of anagrams according to the above requirements.'''


def group_anagrams(strings):
    anagram_groups = {}  # Create an empty dictionary to store the anagram groups
    for string in strings:  # Iterate over each string in the input list 'strings'
        canonical = ''.join(sorted(string))  # Step 1: Sort the characters of the current string and join them back into a single string.
        
        # Step 2: Check if the sorted string ('canonical') is already a key in the 'anagram_groups' dictionary
        if canonical in anagram_groups:
            # If it is, that means we have encountered an anagram of a previously processed string.
            # So, we append the current string to the list of anagrams for that 'canonical' key.
            anagram_groups[canonical].append(string)
        else:
            # If it's not a key in the dictionary, this means we are encountering this 'canonical' pattern for the first time.
            # So, we create a new key-value pair in the 'anagram_groups' dictionary, where the key is 'canonical',
            # and the value is a list containing only the current string (since it's the first occurrence of this anagram).
            anagram_groups[canonical] = [string]
    
    # Finally, after processing all the strings, we return the values of the 'anagram_groups' dictionary as a list.
    # Each value in this list is a group of anagrams represented as a list of strings.
    return list(anagram_groups.values())
    
    
    '''It has a time complexity of O(n * k log k), where n is the length of the input array and k is the maximum length of a string in the input array.  The time complexity comes from sorting each string in the array, which takes O(k log k) time, and the loop that goes through each string in the array, which takes O(n) time.
'''

print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )
