
# METHOD 1 (Big 0 = O(n^2))

# def commonItem(list1, list2):
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 return True
#     return False


# METHOD 2 ( Big 0 = O(n))

def commonItem(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
        
    for j in list2:
        if j in my_dict:
            return True
        
    return False
        


list1 = [1,3,5]
list2 = [2,3,6]

print(commonItem(list1, list2))
        