import random

number = random.randint(1, 100)
print(number)
while True:
    user_number = int(input("Enter a number: "))

    print(number)
    if number == user_number:
        print("You are winner")
        break
    elif number < user_number:
        print("your num is bigger")
    else:
        print("your number is smaller")
