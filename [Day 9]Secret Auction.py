import os


def find_highest_bidder():
    """_summary_

    Returns:
        _type_: _description_
    """
    highest_bid = 0
    highest_bidder = ""
    for key in auction_user_bid:

        if highest_bid < auction_user_bid[key]:
            highest_bid = auction_user_bid[key]
            highest_bidder = key

    print(f"The winner is {highest_bidder} with ${highest_bid}")


print("Welcome to the secret auction program.")
auction_user_bid = {}

next_user = ""
while next_user != "yes":
    user_name = input("What is your name?: ")
    user_bid = int(input("Enter the amount you want to bid: "))
    next_user = input(
        "Are you the last bidder? Type 'yes' to stop the auction: ").lower()
    auction_user_bid[user_name] = user_bid
    os.system('cls')

find_highest_bidder()
