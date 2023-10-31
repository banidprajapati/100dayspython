import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
dict = {value.letter: value.code for key, value in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your name: ").upper()


result = [dict[i] for i in user_input]
print(result)
