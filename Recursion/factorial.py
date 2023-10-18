print("Welcome to the testing factorial function department")
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)
# Base case: 1! = 1
# Test Case 1: Factorial of 0 should be 1
print("---------------------------------------------------------------------")
print("Running Test 1")
print(factorial(0))

# Test Case 2: Factorial of a positive integer (e.g., 5)
print("---------------------------------------------------------------------")
print("Running Test 2")
print(factorial(5))

# Test Case 3: Factorial of a larger positive integer (e.g., 10)
print("---------------------------------------------------------------------")
print("Running Test 3")
print(factorial(10))

# Test Case 4: Factorial of 1 should be 1
print("---------------------------------------------------------------------")
print("Running Test 4")
print(factorial(1))
