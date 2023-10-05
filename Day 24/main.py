with open("./Input/Letters/starting_letter.txt") as letter:
    content = letter.read()

with open("./Input/Names/invited_names.txt") as names:
    for i in names.readlines():
        i = i.strip()
        new_content = content.replace("[name]", i)

        with open(f"./Output/ReadyToSend/letter_for_{i}.txt", mode="w") as file:
            file.write(new_content)
