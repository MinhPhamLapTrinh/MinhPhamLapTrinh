print("Welcome to RECURSIVE LINEAR SEARCH")

# Step 1 : Search for the key that match the index of the list
def check_output(list, key):
    print(f"The given list is: {list if len(list) < 100 else []} and the target is: {key}")
    if linear_search(list, key) == -1:
        print("The target is not in the list")
    else:
        print(f"The position of the key: {linear_search(list, key)}")

def linear_search(my_list, key):
    return recursive_linear_search(my_list, key, 0)

# Step 2 : The argument list is missing the index so cannot go through the list


def recursive_linear_search(list, key, index):
    # Step 3 : BASE CASE return the index when its value matches the key and the key is not found
    if index > (len(list) - 1):
        return -1
    elif key == list[index]:
        return index
    else:
        return (recursive_linear_search(list, key, index + 1))

# Test Case 1: Basic Test
arr1 = [1, 2, 3, 4, 5]
target1 = 3
# Expected Output: 2 (index of the target element in the array)
print("---------------------------------------------------------------------")
print("Running Test 1")
check_output(arr1, target1)
# Test Case 2: Target not in the array
arr2 = [10, 20, 30, 40, 50]
target2 = 25
# Expected Output: -1 (target is not in the array)
print("---------------------------------------------------------------------")
print("Running Test 2")
check_output(arr2, target2)
# Test Case 3: Empty Array
arr3 = []
target3 = 5
# Expected Output: -1 (target is not in the empty array)
print("---------------------------------------------------------------------")
print("Running Test 3")
check_output(arr3, target3)
# Test Case 4: Duplicate Elements
arr4 = [5, 10, 15, 10, 20, 25]
target4 = 10
# Expected Output: 1 (index of the first occurrence of the target)
print("---------------------------------------------------------------------")
print("Running Test 4")
check_output(arr4, target4)
# Test Case 5: Target at the Beginning
arr5 = [100, 200, 300, 400, 500]
target5 = 100
# Expected Output: 0 (target is at the beginning of the array)
print("---------------------------------------------------------------------")
print("Running Test 5")
check_output(arr5, target5)
# Test Case 6: Target at the End
arr6 = [3, 6, 9, 12, 15, 18]
target6 = 18
# Expected Output: 5 (target is at the end of the array)
print("---------------------------------------------------------------------")
print("Running Test 6")
check_output(arr6, target6)
# Test Case 7: Large Array
arr7 = list(range(1, 10001))
target7 = 789
# Expected Output: 788 (target is at index 788 in the array)
print("---------------------------------------------------------------------")
print("Running Test 7")
check_output(arr7, target7)