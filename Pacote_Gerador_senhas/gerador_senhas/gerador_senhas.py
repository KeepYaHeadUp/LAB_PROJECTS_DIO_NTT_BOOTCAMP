import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_l = int(input("How many letters would you like in your password?\n"))
nr_s = int(input("How many symbols would you like?\n"))
nr_n = int(input("How many numbers would you like?\n"))

pas = []
for letter_index in range(nr_l):
  letter_index = random.randint(1, len(letters) - 1)
  pas.append(letters[letter_index])

for number_index in range(nr_n):
  number_index = random.randint(1, len(numbers) - 1)
  pas.append(numbers[number_index])

for symbol_index in range(nr_s):
  symbol_index = random.randint(1, len(symbols) - 1)
  pas.append(symbols[symbol_index])

random.shuffle(pas)

password = ""
for char in pas:
  password += char

print(password)
