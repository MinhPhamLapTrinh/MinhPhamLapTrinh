art = """
         |
         |      /
         |     /
         |    /
         |   /
         |  /
         | /  
         |/_____________________    

         linear search                                                                
"""
print(art)


def final_result(result, key_value):
    if result != -1:
        return print(f"Element {key_value} found at index {result}.")
    else:
        return print(f"Element {key_value} not found in the list.")
# let n represent the length of my list
# let T(n) represent the number of operations done by the function when given a list size n

def linear_search(my_list, key):
    for i in range(0, len(my_list)): # n + 1 + 1
        if my_list[i] == key:        # n
            return i                 # 1
    return -1 # worst case
# T(n) = n + 1 + 1 + n + 1
#      = 2n + 3
# Therefore T(n) is O(n)

print("First Test Case")
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target_value = 5

result = linear_search(my_list, target_value)
final_result(result, target_value)
print("Second Test Case")
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target_value = -1

result = linear_search(my_list, target_value)
final_result(result, target_value)