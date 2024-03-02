n=int(input("Enter the Number="))
sum = 0
t=n
while t > 0:
    a = t % 10
    sum = sum + a **3
    t= t//10
if n == sum:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")
    