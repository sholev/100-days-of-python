import data
from data import MENU, FORMAT_RESOURCES, COIN_VALUES


def get_prompt():
    return f"What would you like? ({"/".join(MENU)}): "


def get_report():
    resources = data.resources
    return FORMAT_RESOURCES.format(resources["water"], resources["milk"],
                                   resources["coffee"], data.profit)


def check_resources(ingredients):
    resources = data.resources
    result = True
    for ingredient in ingredients:
        if (ingredient not in resources or
                ingredients[ingredient] > resources[ingredient]):
            result = False
            print(f"Sorry there is not enough {ingredient}.")
    return result


def process_coins():
    coins = input(f"Enter coins ({",".join(COIN_VALUES)}): ").split(",")
    total_value = 0.0
    for coin_type in coins:
        coin_type = coin_type.lower().strip()
        if coin_type in COIN_VALUES:
            total_value += COIN_VALUES[coin_type]
    return total_value


def process_order(choice):
    choice_data = MENU[choice]
    ingredients = choice_data["ingredients"]
    cost = choice_data["cost"]
    print(f"Cost: ${cost}")
    if check_resources(ingredients):
        data.current_money += process_coins()
        if cost > data.current_money:
            if data.current_money > 0:
                print(f"Sorry that's not enough money. Money refunded: {
                    data.current_money}")
                data.current_money = 0.0
        else:
            data.current_money -= cost
            data.profit += cost
            for ingredient in ingredients:
                data.resources[ingredient] -= ingredients[ingredient]
            if data.current_money > 0:
                print(f"“Here is ${data.current_money} dollars in change.")
                data.current_money = 0
            print(f"Here is your {choice}. Enjoy!")


def main_loop():
    while True:
        choice = input(get_prompt())
        if choice == "off":
            print("Turning off.")
            break
        elif choice == "report":
            print(get_report())
        elif choice in MENU:
            process_order(choice)
        else:
            print("Invalid input.")


main_loop()
