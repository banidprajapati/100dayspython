print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Do you want to go Left or Right? \n")

if direction.lower() == "left":
    print("You see a lake infront of you.")
    action = input("Swim or Wait?\n")
    if action.lower() == "wait":
        print("3 doors appear infront of you while waiting.")
        print("Which door do you want to pick?")
        choice = input("Red, Yellow, Blue?\n")
        if choice.lower() == "yellow":
            print("You Win!")
        elif choice.lower() == "red":
            print("You fell into a pit of fire.")
            print("You died by burning.")
        elif choice.lower() == "green":
            print("Your fell into a pit with a beast.")
            print("Your were eaten by the beast.")
        else:
            print("Game Over!")
    else:
        print("You swimming across the lake you were attacked by Trout.")
        print("Game Over.")
else:
    print("You fell into a hole.")
    print("Game Over.")
