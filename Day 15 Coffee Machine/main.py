import art
import data
import os

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


def check_user_input():
    print("---------------------------------------------------------------------------")
    user_input = ''
    while user_input != "1" and user_input != "2" and user_input != "3" and user_input != "refill" and user_input != "resources":
        user_input = input(
            "Please press a button.\n1 - Espresso\n2 - Latte\n3 - Cappuccino\n: ")

    if user_input == "1":
        ingredients = MENU["espresso"]["ingredients"]
        resources_machine(ingredients)
        cost = MENU["espresso"]["cost"]
        print(f"The cost for Espresso is {cost}.")
        cost_count(cost)
    elif user_input == "2":
        ingredients = MENU["espresso"]["ingredients"]
        resources_machine(ingredients)
        cost = MENU["latte"]["cost"]
        print(f"The cost for Espresso is {cost}.")
        cost_count(cost)
    elif user_input == "3":
        ingredients = MENU["espresso"]["ingredients"]
        resources_machine(ingredients)
        cost = MENU["cappuccino"]["cost"]
        print(f"The cost for Espresso is {cost}.")
        cost_count(cost)
    elif user_input == "refill":
        data.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    elif user_input == "resources":
        print(data.resources)
    else:
        print("Error.")


def cost_count(cost):
    print("Please insert the coin.")
    coin_type1 = int(input("Penny: "))
    coin_type2 = int(input("Nickel: "))
    coin_type3 = int(input("Dime:  "))
    coin_type4 = int(input("Quarter: "))
    total_coin = coin_type1 * 0.01 + coin_type2 * \
        0.05 + coin_type3 * 0.10 + coin_type4 * 0.25

    if total_coin > cost:
        coin_return = total_coin - cost
        print(
            f"You inserted ${total_coin}. Here is your changes. ${coin_return}")
        print("Thank you for making your coffee with us.")
        check_user_input()

    elif total_coin < cost:
        print(
            f"Not enough coin was inserted. The total cost is ${cost}. You only inserted ${total_coin:.2f}.")
        print("Transaction Failed.")
        print(f"Please take your changes ${total_coin}")

    else:
        print("Thank you for making your coffee with us.")
        os.system("cls")
        check_user_input()


def resources_machine(ingredients):
    for i in ingredients:
        print(i)
        data.resources[i] -= ingredients[i]
        if data.resources[i] < ingredients[i]:
            print("Insufficient ingredients. Sorry")


check_user_input()
