import random

print("Добро пожаловать в нашу игру!!!")

number = random.randint(1, 10)

user_number = 0

i = 0

while user_number != number:
    user_number = int(input("Введиите число от 1 до 100: "))
    if user_number < number:
        print("Ваше число меньше, чем искомое")
    elif user_number > number:
        print("Ваше число больше, чем искомое")
    i += 1

print(f"Ты угада число, за число попыток: {i}")
