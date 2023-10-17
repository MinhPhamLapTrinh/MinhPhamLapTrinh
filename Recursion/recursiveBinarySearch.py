print("Welcome to RECURSIVE BINARY SEARCH")
def check_output(list, key):
    print(f"The given list is: {list if len(list) < 100 else []} and the target is: {key}")
    if binary_search(list, key) == -1:
        print("The target is not in the list")
    else:
        print(f"The position of the key: {binary_search(list, key)}")
# step 1 : Return the key by split the list in half and check each index to match the key
def binary_search(my_list, key):
    return recursive_binary_search(my_list, key, 0, len(my_list) - 1)
# step 2 : The argument list of the binary_search function is not enough for searching each index of the list
def recursive_binary_search(my_list, key, low, high):
    mid = (low + high) // 2
    if low > high:
        return -1
    elif key < my_list[mid]:
        return recursive_binary_search(my_list, key, low, mid - 1)
    elif key > my_list[mid]:
        return recursive_binary_search(my_list, key, mid + 1, high)
    else: 
        return mid
    
# Test Case 1: Basic Test - Target is in the middle
arr1 = [1, 2, 3, 4, 5, 6, 7]
target1 = 4
# Expected Output: 3 (index of the target element in the sorted array)
print("---------------------------------------------------------------------")
print("Running Test 1")
check_output(arr1, target1)

# Test Case 2: Target is the first element
arr2 = [10, 20, 30, 40, 50]
target2 = 10
# Expected Output: 0 (target is at the beginning of the sorted array)
print("---------------------------------------------------------------------")
print("Running Test 2")
check_output(arr2, target2)

# Test Case 3: Target is the last element
arr3 = [10, 20, 30, 40, 50]
target3 = 50
# Expected Output: 4 (target is at the end of the sorted array)
print("---------------------------------------------------------------------")
print("Running Test 3")
check_output(arr3, target3)

# Test Case 4: Target is not in the array
arr4 = [2, 4, 6, 8, 10]
target4 = 5
# Expected Output: -1 (target is not in the array)
print("---------------------------------------------------------------------")
print("Running Test 4")
check_output(arr4, target4)

# Test Case 5: Empty Array
arr5 = []
target5 = 7
# Expected Output: -1 (target is not in the empty array)
print("---------------------------------------------------------------------")
print("Running Test 5")
check_output(arr5, target5)

# Test Case 6: Large Array
arr6 = list(range(1, 10001))
target6 = 789
# Expected Output: 788 (target is at index 788 in the sorted array)
print("---------------------------------------------------------------------")
print("Running Test 6")
check_output(arr6, target6)

# Test Case 7: Duplicate Elements
arr7 = [5, 10, 15, 15, 20, 25]
target7 = 15
# Expected Output: 2 (index of the first occurrence of the target)
print("---------------------------------------------------------------------")
print("Running Test 7")
check_output(arr7, target7)
