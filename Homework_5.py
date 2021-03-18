# Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def multiply(numbers):  
    a = 1
    for x in numbers:
        a = a * x
    return a

print(multiply([1,2,3,-4]))

print(multiply([0,2,3,-4]))

print(multiply([1,1,1,-1]))