''' find all the numbers between 1000 and 3000 (both
excluded) such that each digit of a number is an odd number. Print the number
of such elements '''

odd_element_list = []
for num in range(1000,3000):
    num_str = str(num)
    flag = True
    for p in range(4):
        if  not int(num_str[p]) in [1,3,5,7,9]:
            flag =False
    if flag :
        odd_element_list.append(num_str)

print(odd_element_list)
