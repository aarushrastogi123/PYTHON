print("Enter the year =",end=' ')
year=int(input())
if(year%400==0):
    print('The year is leap year')
elif(year%100==0):
    print('The year is not a leap year')
elif(year%4==0):
    print("The year is a leap year")
else:
    print("The leap is not a leap year")

