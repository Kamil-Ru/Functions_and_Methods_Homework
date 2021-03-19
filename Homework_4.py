# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_list(lst):
    return list(set(lst))
    
# TEST
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))



###      answer from Udemy

def unique_list_2(lst):
    # Also possible to use list(set())
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x

print(unique_list_2([1,1,1,1,2,2,3,3,3,3,4,5]))
