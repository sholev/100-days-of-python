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

FORMAT_RESOURCES = """Water: {0}ml
Milk: {1}ml
Coffee: {2}g
Profit: ${3}"""

COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "pennie": 0.01,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

current_money = 0.0
profit = 0.0
