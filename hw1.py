while True:
    users_num = int(input("enter a number"))
    if users_num >= 0 and users_num <= 10:
        print(users_num ** 2)
    else:
        continue
name = input("enter your name")
surname = input("enter your surname")
age = int(input("enter your age"))
weight = int(input("enter your weight"))

if age <= 30 and weight <= 120 and weight >= 50:
    print("you are in good fit")
elif age > 30 and weight > 120 and weight < 50:
    print("you should work on yourself")
elif age > 40 and weight > 120 and weight < 50:
    print("You have to visit a doctor")
else:
    print("are your ready for it?")