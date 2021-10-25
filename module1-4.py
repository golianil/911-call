'''
accepts a string and calculates the number of letters
and digits
'''

string = input("Enter any string with digits ")

str_upper = string.upper()
alpha_count = 0
num_count = 0
for st in str_upper:
    if st.isupper():
        alpha_count = alpha_count + 1
    elif st.isdigit():
        num_count = num_count + 1

print(f'Alphabets in {string} - {alpha_count}')
print(f'numbers in {string} - {num_count}')
