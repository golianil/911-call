''' print the factorail of and print if even or odd '''

n = 100
for r in range(1,100):
    if n % r == 0:
        if r % 2 == 0:
            print(f'{r} is even factor of {n}')
        else:
            print(f'{r} is odd factor of {n}' )
