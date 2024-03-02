print("The Love Calculator is calculating your score...")
name1 = input("Enter the first name: ") # What is your name?
name2 = input("Enter the second name: ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
a= name1+name2
b= a.lower()
t=b.count("t")
r=b.count("r")
u=b.count("u")
e=b.count("e")
first_digit=t+r+u+e

l=b.count("l")
o=b.count("o")
v=b.count("v")
e=b.count("e")
second_digit=l+o+v+e

c=int(str(first_digit)+str(second_digit))
if(c<10 or c>90):
    print(f"Your score is {c}, you go together like coke and mentos.")
elif(40<=c<=50):
    print(f"Your score is {c}, you are alright together.")
else:
    print(f"Your score is {c}.")     