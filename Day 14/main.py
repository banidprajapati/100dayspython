import art
import data
import random

total_score = 0
print(art.logo)

data_A = random.randint(0, 49)
data_B = random.randint(0, 49)


def main(data_A, data_B):
    global total_score
    print("A:")
    print(
        f"{data.data[data_A]['name']}, A {data.data[data_A]['description']} from {data.data[data_A]['country']}")
    print("\nOR\n")
    print("B:")
    print(
        f"{data.data[data_B]['name']}, A {data.data[data_B]['description']} from {data.data[data_B]['country']}\n")

    if check_condition(get_user_input(), data_A, data_B):
        total_score += 1
        print("__________________________")
        data_A = data_B
        data_B = random.randint(0, 49)
        main(data_A, data_B)

    else:
        print('Game Over')


def get_user_input():
    user_guess = input("A or B: ").lower()
    while user_guess != 'a' and user_guess != 'b':
        print("The only valid inputs are 'A' or 'B'.")
        user_guess = input("A or B: ").lower()
    return user_guess


def check_condition(user_guess, int_a, int_b):
    if user_guess == 'a':
        if (data.data[int_a]['follower_count']) > (data.data[int_b]['follower_count']):
            return True
    else:
        if (data.data[data_A]['follower_count']) < (data.data[int_b]['follower_count']):
            return int_a


print("Welcome to Higher Lower game.\n")
main(data_A, data_B)
print(f"Your total score: {total_score}")
