from main import MENU, resources

espresso_info = MENU["espresso"]
latte_info = MENU["latte"]
cappuccino_info = MENU["cappuccino"]

user_pays = 0

#RESOURCE TRACKING
total_profit = 0

def add_coins (quarters, dimes, nickel, pennies):
    q = float(quarters * 0.25)
    d = float(dimes * 0.10)
    n = float(nickel * 0.05)
    p = float(pennies * 0.01)
    return( q + d + n + p)

def compare_prices (coin_total, coffee_price):
    if coin_total < coffee_price:
        return "Not Enough"
    else:
        return"Thank you"

user_order = input("What would you like? (espresso/latte/capuccino): ")

if user_order == "espresso":
    user_pays = espresso_info["cost"]
elif user_order == "latte":
    user_pays = latte_info["cost"]
elif user_order == "cappucino":
    user_pays = cappuccino_info["cost"]
elif user_order == "report":
    user_pays = 1000

print("Please insert coins.")
quarters = float(input("how many quarters?: "))
dimes = float(input("how many dimes?: "))
nickles = float(input("how many nickles?: "))
pennies = float(input("how many pennies?: "))

coin_total = add_coins(quarters, dimes, nickles, pennies)
is_enough = compare_prices(coin_total, user_pays)

print(is_enough)

