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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_user_input():
    print("---------------------------------------------------------------------------")
    is_on = True

    while is_on:
        user_input = input(
            "Menu:\nEspresso\nLatte\nCappuccino\n: ").lower()

        if user_input == "espresso" or user_input == "cappuccino" or user_input == "latte":
            ingredients = MENU[user_input]["ingredients"]
            cost = MENU[user_input]["cost"]
            resources_machine(ingredients)
            print(f"The cost for {user_input.title()} is {cost}.")
            cost_count(cost)

        elif user_input == "off":
            is_on = False

        elif user_input == "resources":
            print(resources)

        else:
            print("Sorry, that item is not available in our menu.")


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

    elif total_coin < cost:
        print(
            f"Not enough coin was inserted. The total cost is ${cost}. You only inserted ${total_coin:.2f}.")
        print("Transaction Failed. Refunding the coins")

    else:
        print("Thank you for making your coffee with us.")


def resources_machine(ingredients):
    for i in ingredients:
        print(i)
        print(ingredients[i])
        if resources[i] < ingredients[i]:
            resources[i] -= ingredients[i]
            print("Insufficient ingredients. Sorry")
            is_on = False


check_user_input()
