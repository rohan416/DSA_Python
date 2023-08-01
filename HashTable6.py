'''Instructions: 
HT: Subarray Sum (⚡Interview Question)
Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).

Your function should take two arguments:

nums: a list of integers representing the input array

target: an integer representing the target sum


Your function should return a list of two integers representing the starting and ending indices of the subarray that adds up to the target sum. If there is no such subarray, your function should return an empty list.

For example:



nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))  # should print [1, 3]


Note that there may be multiple subarrays that add up to the target sum, but your function only needs to return the indices of any one such subarray. Also, the input list may contain both positive and negative integers.'''

def subarray_sum(nums, target):
    sum_index = { 0 : -1}
    curr_sum = 0
    for i , num in enumerate(nums):
        curr_sum += num
        if curr_sum - target in sum_index:
            return [sum_index[curr_sum- target] + 1, i]
        sum_index[curr_sum] = i
    return []
    
    
    '''Overall, the function has a time complexity of O(n) because it loops through the input list exactly once. The space complexity of the function is also O(n), since the sum_index hash table can potentially store all n elements of the input list.
'''
    
nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )