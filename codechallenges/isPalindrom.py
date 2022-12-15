# check if the string is a palindrome. 

import re



def is_palindrome(string):
    # clean up string
    regular = ''.join(re.findall(r'[a-z]+', string.lower()))
    reversed = regular[::-1]
    return reversed == regular

print(is_palindrome("Go hang a salami - I'm a lasagna hog"))