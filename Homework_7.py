# Hard:
# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
# Hint: You may want to use .replace() method to get rid of spaces.

# Hint: Look at the string module

# Hint: In case you want to use set comparisons

##### My Notes
'''
import string
alphabet=string.ascii_lowercase

str1 = "The quick brown fox jumps over the lazy"
str2 = str1.replace(' ','')
str2 = str2.lower()
str2 = set(str2)
alphabet=set(string.ascii_lowercase)

if alphabet.issubset(str2):
    print('OK')
else:
    print('nop')


'''

import string

def ispangram(str1, alphabet=set(string.ascii_lowercase)):
    str2 = set(str1.replace(' ','').lower())

    if alphabet.issubset(str2):
        print('"{}" is a pangram.'.format(str1))
    else:
        print('"{}" is not a pangram.'.format(str1))

## TEST
ispangram("The quick brown fox jumps over the lazy dog")
ispangram("The quick brown fox jumps over the lazy DOG")
ispangram("The quick brown fox jumps over the lazy")
ispangram("Jackdaws love my big sphinx of quartz")
ispangram("Pack my box with five dozen liquor jugs")




