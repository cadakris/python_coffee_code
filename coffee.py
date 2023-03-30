from main import MENU, resources

espresso_info = MENU["espresso"]
latte_info = MENU["latte"]
cappuccino = MENU["cappuccino"]


user_order = input("What would you like? (espresso/latte/capuccino): ")

user_pays = 0

#RESOURCE TRACKING
total_profit = 0

if user_order == "espresso":
    user_pays = espresso_info["cost"]
elif user_order == "latte":
    user_pays == latte_info["cost"]

print(user_pays)
