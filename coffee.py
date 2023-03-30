from main import MENU, resources

espresso_info = MENU["espresso"]
latte_info = MENU["latte"]
cappuccino_info = MENU["cappuccino"]

user_pays = 0

#RESOURCE TRACKING
total_profit = 0

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
quarters = input("how many quarters?: ")
dimes = input("how many dimes?: ")
nickles = input("how many nickles?: ")
pennies = input("how many pennies?: ")



