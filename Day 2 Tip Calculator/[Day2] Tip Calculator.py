print("Welcome to the tip calculator.")
totalBill = float(input("What is your total bill? "))
totalPerson = int(input("How many people to split the bill? "))
tipPercent = int(input(
    "What percentage tip would you like to give? 10, 12, or 15? "))

result = ((totalBill*tipPercent/100)+totalBill)/totalPerson
print(round(result,21))
