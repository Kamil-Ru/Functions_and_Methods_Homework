# Write a Python function that checks whether a word or phrase is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". 
# Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. 
# Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.


def palindrome(s):
    pali = s
    pali = pali.replace(' ','')
    pali = pali.replace(',','')
    pali = pali.replace("’",'')
    pali = pali.lower()

    if pali == pali [::-1]:
        return print('"{}" is palidrome'.format(s))
    else:
        return print('"{}" is NOT palidrome'.format(s))

palindrome('helleh')
palindrome('nurses run')
palindrome('Madam, I’m Adam')

# OR:





    




