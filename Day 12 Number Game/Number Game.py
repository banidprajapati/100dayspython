import art
import random

print(art.logo)
print("I am thinking of a number between 1 to 100.")
print("You have 15 guesses to find the number I am thinking of")
random_number = random.randint(1, 100)


def win_condition():
    if guess == random_number:
        print(
            f"You guessed it. The number I was thinking of was {random_number}")
        exit()
    elif guess > random_number:
        print("Too high")
    elif guess < random_number:
        print("Too low.")


guess_chance = 0
while guess_chance != 15:
    guess = int(input("Guess a number: "))
    win_condition()
    guess_chance += 1
print(f"Game over. The number I was thinking of was {random_number}")
