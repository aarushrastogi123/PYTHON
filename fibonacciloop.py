a=int(input('Enter the number of terms='))
t1=0
t2=1
t3=t1+t2
print(t1)
print(t2)
print(t3)
for I in range(3,a):
    
    t1=t2
    t2=t3
    t3=t1+t2
    print(t3)
    I+1

