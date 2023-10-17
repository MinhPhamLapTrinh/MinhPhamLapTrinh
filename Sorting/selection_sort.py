print("Welcome to Selection Sort")
def selection_sort(my_list):
    temp = 0
    n = len(my_list)
    for i in range(n - 1):
        minIdx = i
        for j in range(i + 1, n):
            if my_list[j] < my_list[minIdx]:
                minIdx = j
        if minIdx != i:
            my_list[i], my_list[minIdx] = my_list[minIdx], my_list[i]
    print(my_list)
# Test Case 1: Basic Test - Random Order
arr1 = [5, 1, 4, 2, 8]
# Expected Output: [1, 2, 4, 5, 8] (sorted in ascending order)
print("------------------------------------------------------------------------------")
print("Test 1")
selection_sort(arr1)

# Test Case 2: Already Sorted in Ascending Order
arr2 = [1, 2, 3, 4, 5]
# Expected Output: [1, 2, 3, 4, 5] (no swaps needed)
print("------------------------------------------------------------------------------")
print("Test 2")
selection_sort(arr2)

# Test Case 3: Already Sorted in Descending Order
arr3 = [5, 4, 3, 2, 1]
# Expected Output: [1, 2, 3, 4, 5] (sorted in ascending order with multiple swaps)
print("------------------------------------------------------------------------------")
print("Test 3")
selection_sort(arr3)

# Test Case 4: Array with Duplicate Elements
arr4 = [3, 1, 2, 3, 5, 2, 4, 4]
# Expected Output: [1, 2, 2, 3, 3, 4, 4, 5] (sorted in ascending order with swaps)
print("------------------------------------------------------------------------------")
print("Test 4")
selection_sort(arr4)

# Test Case 5: Empty Array
arr5 = []
# Expected Output: [] (no elements to sort)
print("------------------------------------------------------------------------------")
print("Test 5")
selection_sort(arr5)

# Test Case 6: Large Array
arr6 = list(range(10000, 0, -1))
# Expected Output: [1, 2, 3, ..., 9999, 10000] (sorted in ascending order with many swaps)
print("------------------------------------------------------------------------------")
print("Test 6")
selection_sort(arr6)