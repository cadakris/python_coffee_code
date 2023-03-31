MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_sufficient_resources(drink):
    '''CHECK TO SEE IF YOU HAVE ENOUGH RESOURCES TO MAKE COFFEE'''
    for ingredient in drink:
        if drink[ingredient] > resources[ingredient]:
            print(f"Sorry, there's not enough {ingredient}.")
            return False
    return True


def calculate_money():
    '''CALCULATE THE TOTAL OF COINS SUBMITTED'''
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?:" )) * 0.01
    return total


def payment_is_successful(payment, cost):
    '''CHECKING IF PAYMENT IS CORRECT'''
    if payment < cost:
        print("Sorry that is not enough money. Money refunded.")
        return False
    else:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True


def make_coffee(order, list_of_ingredients):
    '''IF EVERYTHING CHECKS OUT - MAKE COFFEE AND SUBTRACT RESOURCES'''
    for ingredient in list_of_ingredients:
        resources[ingredient] -= list_of_ingredients[ingredient]
    print(f"Here is your {order}. Enjoy!")


is_coffee_maker_on = True

while is_coffee_maker_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == "off":
        is_coffee_maker_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
    else:
        drink = MENU[user_choice]
        if is_sufficient_resources(drink['ingredients']):
            user_paid = calculate_money()
            if payment_is_successful(user_paid, drink['cost']):
                make_coffee(user_choice, drink['ingredients'])
