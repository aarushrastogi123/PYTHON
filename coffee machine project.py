MENU = {

    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 55.50,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 82.50,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 93.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_sufficient(order_ingredients):
    
    for i in order_ingredients:
        
        if order_ingredients[i]>=resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
        
        return True

def amount():
        print('Please insert money.')
        ruppees=int(input("how many ruppees: "))
        paise=int(input("how many paise: "))
        money=ruppees+(paise/100)
        if money>drink["cost"]:
            global profit
            remaining=round(money-drink["cost"],2)
            profit+=drink["cost"]
            print(f"\n Here is your change: {remaining}.\n Enjoy your {choice}!")
        elif money<drink["cost"]:
            print(f"\n Sorry that's not enough money. Here's your refund.")

def deduction(left_items):
    for i in left_items:
        resources[i]-=left_items[i]

on = True

while on:
    
    choice=input("What would you like? (espresso/cappuccino/latte): ")
    
    if choice=="off":
        on=False
    
    elif choice=="report":
        deduction(drink["ingredients"])
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs: {profit}/-")
        
    else:
        drink=MENU[choice]
        if is_sufficient(drink["ingredients"]):
            amount()


            