import random

from click import clear

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

used_letters=0
used_symbols=0
used_numbers=0
pswrd = ""

for letter in range(0, nr_letters+nr_symbols+nr_numbers):
    x = random.randint(0,2)
    if x == 0 and used_letters != nr_letters:
        pswrd = pswrd + str(random.choice(letters))
        used_letters+=1
    elif x == 1 and used_symbols != nr_symbols:
        pswrd = pswrd + str(random.choice(symbols))
        used_symbols+=1
    elif x == 2 and used_numbers != nr_numbers:
        pswrd = pswrd + str(random.choice(numbers))
        used_numbers+=1
    else:
        if used_letters != nr_letters:
            pswrd = pswrd + str(random.choice(letters))
            used_letters += 1
        elif used_symbols != nr_symbols:
            pswrd = pswrd + str(random.choice(symbols))
            used_symbols += 1
        elif used_numbers != nr_numbers:
            pswrd = pswrd + str(random.choice(numbers))
            used_numbers += 1

print(f"Your Password is-->  " + pswrd)