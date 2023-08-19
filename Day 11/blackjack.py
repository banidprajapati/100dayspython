import art
import random
import os

cards_list = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
users_hand = []
dealers_hand = []


def play_again():
    os.system('cls')
    users_hand.clear()
    dealers_hand.clear()
    print(art.logo)

    dealers_hand.append(random.choice(cards_list))
    dealers_total = number_switch(dealers_hand)
    print(f"\nDealers hand: {dealers_hand} Total:{dealers_total}")

    for _ in range(2):
        users_hand.append(random.choice(cards_list))
    users_total = number_switch(users_hand)
    print(f"\nYour hand: {users_hand} Total:{users_total}")

    users_side()
    dealers_side()
    win_condition(users_total, dealers_total)


def number_switch(hands):
    fake_hands = list(hands)
    for i in range(len(fake_hands)):
        if fake_hands[i] == "J" or fake_hands[i] == "Q" or fake_hands[i] == "K":
            fake_hands[i] = 10
        elif fake_hands[i] == "A":
            fake_hands[i] = 11

    total = sum(fake_hands)
    if total > 21:
        for i in range(len(fake_hands)):
            if fake_hands[i] == 11:
                fake_hands[i] = 1
                total -= 10
    return total


def users_side():
    user_choice = input(
        "\nDo you want to hit or stand?\nType '1' for 'HIT'\nType '2' for 'STAND'\n- ")
    while user_choice == '1':
        users_hand.append(random.choice(cards_list))
        print(f"\nYour hand: {users_hand} Total:{number_switch(users_hand)}")

        if number_switch(users_hand) > 21:
            print("Bust. You lose")
            play_over = input(
                "Do you want to play again. Type 'y' for another hand: ")
            if play_over == 'y':
                play_again()
            else:
                exit()
        elif number_switch(users_hand) == 21:
            print("You win")
            play_over = input(
                "Do you want to play again. Type 'y' for another hand: ")
            if play_over == 'y':
                play_again()
            else:
                exit()

        user_choice = input(
            "Do you want to hit or stand?\nType '1' for 'HIT'\nType '2' for 'STAND'\n- ")
    print(
        f"\nYour final hand: {users_hand} Total:{number_switch(users_hand)}")


def dealers_side():
    while number_switch(dealers_hand) < 18 and number_switch(dealers_hand) <= number_switch(users_hand):
        dealers_hand.append(random.choice(cards_list))
        print(
            f"\nDealer's hand: {dealers_hand} Total:{number_switch(dealers_hand)}")
        if number_switch(dealers_hand) > 21:
            print("Dealer went over. You win")
            play_over = input(
                "Do you want to play again. Type 'y' for another hand: ")
            if play_over == 'y':
                play_again()
            else:
                exit()
        elif number_switch(dealers_hand) == 21:
            print("You lost")
            play_over = input(
                "Do you want to play again. Type 'y' for another hand: ")
            if play_over == 'y':
                play_again()
            else:
                exit()
    print(
        f"\nDealer's final hand: {dealers_hand} Total:{number_switch(dealers_hand)}")


def win_condition(users_total, dealers_total):
    if users_total < dealers_total:
        print("You win!")
    elif users_total == dealers_total:
        print("Draw")
    else:
        print("You lost.")
    play_over = input("Do you want to play again. Type 'y' for another hand: ")
    if play_over == 'y':
        play_again()
    else:
        exit()


play_again()
