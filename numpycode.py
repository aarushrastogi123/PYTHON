import numpy as n
a=n.array([1,2,3,4,5,6,7,8,9])
print('a=',a)
b=a.reshape(3,3)
print('b=\n',b)
c=a.max()
print(c)
d=a.min()
print(d)
e=a.reshape(3,3)
print(b+e)
for i in b:
    print(i)
    for j in i:
        print(j)
        
  
