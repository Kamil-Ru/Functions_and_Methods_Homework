# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    if low <= num <= high:
        return print('{} is in the range between {} and {}.'.format(num,low,high))
    else:
        return print('{} is NOT in the range between {} and {}.'.format(num,low,high))
    
ran_check(10,2,7)
ran_check(5,2,7)
ran_check(7,2,7)
