import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock, Paper, Scissors, Shoot!")
choice = int(input("1 - Rock\n2 - Paper\n3- Scissor\nType 1, 2 or 3: "))
if choice == 1:
    print(f"You picked Rock\n{rock}")
elif choice == 2:
    print(f"You picked Paper\n{paper}")
elif choice == 3:
    print(f"You picked Scissors\n{scissors}")
else:
    print("Please enter a valid number")


computer_choice = random.randint(1, 3)

if computer_choice == 1:
    print(f"Computer picked Rock\n{rock}")
elif computer_choice == 2:
    print(f"Computer picked Paper\n{paper}")
else:
    print(f"Computer picked Scissors\n{scissors}")

if choice == 2 and computer_choice == 1:
    print("You Win!")
elif choice == 3 and computer_choice == 2:
    print("You Win!")
elif choice == 1 and computer_choice == 3:
    print("You Win!")
elif choice == computer_choice:
    print("Draw")
else:
    print("You Lost!")
