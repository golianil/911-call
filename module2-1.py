'''
built-in rules for checking the validity of the passwords entered by the users.
Following are the rules for checking the validity of a password:
At least 1 alphabet
At least 1 digit between [0-9]
At least 1 character from [@&]
Minimum length of transaction password: 5
Maximum length of transaction password: 10
'''
import re
password = input("Enter the password ")
p_len = len(password)
_pattern = re.compile('(^(.[a-z])+[.\d]+.[@|&]+){5,10})$')

print(re.search(_pattern, password))
   

