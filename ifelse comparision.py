print('ENTER THE THREE NUMBERS=')
a=float(input())
b=float(input())
c=float(input())
print(a,b,c)
if(b>a):
    if(b>c):
        print(b,'GREATEST')
    else:
        print(c,'GREATEST')
else:
    if(a>c):
        print(a,"GREATEST")
    else:
        print(c,'GREATEST')


