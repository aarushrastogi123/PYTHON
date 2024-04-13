print("___THE__CALCULATOR___")
import os
from time import sleep
def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide,
}
def calculator():
    a=float(input("What is the first number: "))
    
    for i in operations:
        print(i)
    
    should_ans=True
    while should_ans:
        c=input("Choose the operations you want to perform: ")
        b=float(input("What is the second number: "))
        calc=operations[c]
        answer=calc(a,b)
        print(f"{a} {c} {b} = {answer}")
        sleep(2)
        os.system('cls')
        if input(f"Do you want to perform any other function with {answer} or start a new calculation (yes/no): ") == 'yes':
            a=answer
        else:
            should_ans=False
            calculator()

calculator()    
