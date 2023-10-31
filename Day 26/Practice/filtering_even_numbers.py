list_of_strings = input().split(',')

numbers = [int(i) for i in list_of_strings]
result = [n for n in numbers if n % 2 == 0]

print(result)
