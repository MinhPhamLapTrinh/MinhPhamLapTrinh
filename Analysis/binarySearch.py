arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
arr1 = [2, 5, 8, 12, 16, 24, 38, 56, 72, 91]
target = 23


# let n is the length of my list
# T(n) represent the number of operations done by the function when given a list size
def binary_search(my_list, key):
    rc = -1 # 1
    low = 0 # 1
    high = len(my_list) - 1 # 1 for assignment 1 for function call 1 for operator -> 3

    # The loop will run one time more than the exponent (log_2 n + 1)
    while rc == -1 and low <= high: # there are 3 operators per iterations 3(log_2 n + 1)
        mid = (low + high) // 2 # 3log(_2 n + 1)
        if key < my_list[mid]: # log(_2 n + 1)
            high = mid - 1
        elif key > my_list[mid]: #log(_2 n + 1)
            low = mid + 1 #2 * log(_2 n + 1)
        else:
            rc = mid
    return rc # 1
# T(n) = 1 + 1 + 3 + 3(log_2 n + 1) + 3(log_2 n + 1) + (log_2 + 1) + (log_2 n + 1) + 2(log_2 n + 1) + 1
#      = 6 + 10(log_2 n + 1)
#      = 6 + 10log_2 n + 10
#      = 16 + 10log_2n
#  Therefore T(n) is O(logn)

print(binary_search(arr, target))
print(binary_search(arr1, target))