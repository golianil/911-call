'''
find whether the given number is Palindrome
'''

number = input("enter the number ")
if (number[:] == number[::-1] ):
    print(f'number is palindrome {number}')
else:
    print(f'number not palindrome')

