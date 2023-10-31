# number = [1, 2, 3]
# new_number = [i + 1 for i in number]
# print(new_number)

# name = "Banid"
# new_name = [i for i in name]
# print(new_name)

# list_of_number = [i * 2 for i in range(1, 5)]
# print(list_of_number)

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# long_names = [name.upper() for name in names if len(name) > 4]
# print(long_names)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# 🚨 Don't change code above 👆
# Write your code below 👇
list_of_words = sentence.split(" ")
result = {key: len(key) for key in list_of_words}


print(list_of_words)
print(result)
