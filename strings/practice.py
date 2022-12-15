# str = input("Write a string: ")

import string

# all hex digits
hex = string.hexdigits

print(f"All hex digits {hex}")

# ascii letters

asc = string.ascii_letters

print(f"All ascii letters {asc}")

#Ascii lowercase letters

asc_lower = string.ascii_lowercase

print(f"All ascii lower case letters {asc_lower}")

#AScii uppercase letters

asc_upper = string.ascii_uppercase

print(f"All ascii upper case letters {asc_upper}")


#Digits as  strings

digits = string.digits

print(f"All digits { digits }")

# Making digits into a list of numbers


list_ints = list(digits)
for x in list_ints:
    x = int(x)
    list_ints[x] = x

print(f'A list of digits as ints { list_ints }')

# All the punctuation 

punc = string.punctuation

print(f"This is the punctuation {punc} ")




