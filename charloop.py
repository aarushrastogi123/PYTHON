print("\nWORD PATTERN")
word='PYTHON'
x=""

for i in word:
    x=x+i
    print(x)

print('\n ALL STAR PATTERN')

for i in range(5):
    for j in range(5):
        print('*',end='')
    print('') 

print('\nSTAR PATTERN')

for i in range(5):
    for j in range(1,i+2):
        print('*',end=' ')
    print(' ') 

print('\nNUMBER PATTERN')

for i in range(5):
    for j in range(1,i+2):
        print(j,end=' ')
    print("")     

print('\nLETTER PATTERN')

for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end=' ')
    print('')    

print('\nREV NUMBER PATTERN')

for i in range(6,1,-1):
    for j in range(1,i):
        print(j,end=' ')
    print(' ')   

print('\nREV STAR PATTERN')

for i in range(5,0,-1):
    for j in range(0,i):
        print('*',end=' ')
    print('')  

print('\nREV LETTER PATTERN')

for i in range(70,65,-1):
    for j in range(65,i):
        print(chr(j),end=' ')
    print('') 

