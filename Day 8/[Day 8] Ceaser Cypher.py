import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo, "\n")
direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
while direction != "encode" and direction != "decode":
    print("Wrong input. Try again!")
    direction = input(
        "Type 'encode' to encrypt or 'decode' to decrypt.").lower()

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
number = []
cipher_text = []


def cypher(plain_text, shift, direction):
    plain_text_list = list(plain_text)  # converting plain text into a list

    for i in plain_text_list:  # taking every index of the list
        for j in range(0, 26):
            # matching index from plain_text_list to alphabet list and saving the numbers from it
            if i == alphabet[j]:
                number.append(j)

    for i in range(0, len(number)):  # numbers from append being added with shift number
        if direction == "encode":
            number[i] += shift
        else:
            number[i] -= shift

        # for looping of the index. If index is more than 25 then this runs. Ex: number[45] then 45 % 26 = 19, s number[45] is t.
        if number[i] > 25:
            number[i] = number[i] % 26

    for i in number:
        cipher_text.append(alphabet[i])  # converting the numbers into letters.
    print("The encoded text is: "+"".join(cipher_text))


cypher(text, shift, direction)
