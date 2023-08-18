import art


def calculator(first, sign, second):
    if sign == "+":
        return first + second
    elif sign == "-":
        return first - second
    elif sign == "*":
        return first * second
    elif sign == "/":
        return first / second
    else:
        return "Error, Try again later."


print(art.logo)
initial_number = int(input("Enter a number: "))

ask_again = 'y'
while ask_again == 'y':
    sign = ''
    while sign != '+' and sign != '-' and sign != '*' and sign != '/':
        sign = input("+\n-\n*\n/\nEnter an operation: ")
    second_number = int(input("Enter a number: "))

    result = calculator(initial_number, sign, second_number)
    print(f"{initial_number} {sign} {second_number} = {result}")
    initial_number = result

    ask_again = input(
        f"Type 'y' to continue calculation with {result}: ").lower()
