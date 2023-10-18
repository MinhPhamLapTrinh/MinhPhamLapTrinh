# Fibonacci sequence: where the first two numbers are 0 and 1, 
#                     with each subsequent number being defined as the 
#                     sum of the previous two numbers in the sequence.
# Src: https://medium.com/launch-school/recursive-fibonnaci-method-explained-d82215c5498e
print("Welcome to the testing FIBONACCI department")
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

print("---------------------------------------------------------------------")
print("Running Test 1")
print(fibonacci(1))

print("---------------------------------------------------------------------")
print("Running Test 2")
print(fibonacci(2))

print("---------------------------------------------------------------------")
print("Running Test 2")
print(fibonacci(4))
# 0 1 1 2 3
#         ^ at the position of 4 is 3

print("---------------------------------------------------------------------")
print("Running Test 5")
print(fibonacci(5))
# 0 1 1 2 3 5 8
#           ^ at the position of 5 start from 0

print("---------------------------------------------------------------------")
print("Running Test 9")
print(fibonacci(9))