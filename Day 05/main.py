import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0' ,'1', '2','3','4','5','6','7','8','9']
characters = ['!','@','#','$','%','^','&','*','(',')','+']

print("Welcome to the Password Generator!")
no_letters = int(input("How many letters would you like? "))
no_numbers = int(input("How many numbers would you like? "))
no_symbols = int(input("How many symbols would you like? "))

password_list = []
for letter in range(0, no_letters):
    password_list.append(random.choice(letters))
for number in range(0, no_numbers):
    password_list.append(random.choice(numbers))
for character in range(0, no_symbols):
    password_list.append(random.choice(characters))
random.shuffle(password_list)

password = ""
for char in password_list:
    password+=char
print(f"Your password could be: {password}")
