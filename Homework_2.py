# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    if low <= num <= high:
        return print('{} is in the range between {} and {}.'.format(num,low,high))
    else:
        return print('{} is NOT in the range between {} and {}.'.format(num,low,high))
    
ran_check(10,2,7)
ran_check(5,2,7)
ran_check(7,2,7)
ran_check(5,0,5)
ran_check(0,0,5)

## Answer from Udemy:

def ran_check_2(num,low,high):
    if num in range(low,high+1):
        print(f'{num} is in range od {low} and {high}')
    else:
        print('not in range')

ran_check_2(10,2,7)
ran_check_2(5,2,7)
ran_check_2(7,2,7)
ran_check_2(5,0,5)
ran_check_2(0,0,5)