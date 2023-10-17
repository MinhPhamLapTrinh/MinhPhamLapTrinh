print("Welcome to Bubble Sort")
def bubble_sort(my_list):
    temp = 0
    for i in range(0, len(my_list) - 1):
        for j in range(len(my_list) - 1 - i):
            if my_list[j] > my_list[j + 1]:
                # temp = my_list[j]
                # my_list[j] = my_list[j + 1]
                # my_list[j + 1] = temp

                # Multiple assignment in Python seperated by comma
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print(my_list)
# Test Case 1: Basic Test - Random Order
arr1 = [5, 1, 4, 2, 8]
# Expected Output: [1, 2, 4, 5, 8] (sorted in ascending order)
print("------------------------------------------------------------------------------")
print("Test 1")
bubble_sort(arr1)

# Test Case 2: Already Sorted in Ascending Order
arr2 = [1, 2, 3, 4, 5]
# Expected Output: [1, 2, 3, 4, 5] (no swaps needed)
print("------------------------------------------------------------------------------")
print("Test 2")
bubble_sort(arr2)

# Test Case 3: Already Sorted in Descending Order
arr3 = [5, 4, 3, 2, 1]
# Expected Output: [1, 2, 3, 4, 5] (sorted in ascending order with multiple swaps)
print("------------------------------------------------------------------------------")
print("Test 3")
bubble_sort(arr3)

# Test Case 4: Array with Duplicate Elements
arr4 = [3, 1, 2, 3, 5, 2, 4, 4]
# Expected Output: [1, 2, 2, 3, 3, 4, 4, 5] (sorted in ascending order with swaps)
print("------------------------------------------------------------------------------")
print("Test 4")
bubble_sort(arr4)

# Test Case 5: Empty Array
arr5 = []
# Expected Output: [] (no elements to sort)
print("------------------------------------------------------------------------------")
print("Test 5")
bubble_sort(arr5)

# Test Case 6: Large Array
arr6 = list(range(10000, 0, -1))
# Expected Output: [1, 2, 3, ..., 9999, 10000] (sorted in ascending order with many swaps)
print("------------------------------------------------------------------------------")
print("Test 6")
bubble_sort(arr6)