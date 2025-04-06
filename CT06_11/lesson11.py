# print("Hello from lesson 11")

# px=int(input("What is the price? "))
# if px <= 5:
#     print("Sounds good!")
# elif px <= 50:
#     print("Are you sure you need this?")
# elif px <= 500:
#     print("Where are you getting this money from?!")
# else:
#     print("Don't even think about it!")

# rider1 = int(input("What is player 1's height: "))
# rider2 = int(input("What is player 2's height: "))
# if rider1 > 120 and rider2 > 120:
#     print("O")
# else:
#     print("X")

# num = int(input("Choose a random number: "))
# if num % 3 == 0 and num % 7 == 0:
#     print("The number is divisible by 3 and 7")

# name1 = input("First name: ")
# name2 = input("Last name: ")
# if name1 == "James" and name2 == "Leong": # need to be string "James"
#     print("You Are WANTED")

# rider1 = int(input("What is player 1's age: "))
# rider2 = int(input("What is player 2's age: "))
# if rider1 >= 18 or rider2 >= 18:
#     print("O")
# else:
#     print("X")

# age = int(input("What is your age: "))
# if age < 12 or age > 65:
#     print("$15")
# else:
#     print("$20")

# var = input("What is your gender: ")
# if var == "M" or var == "Male":
#     print("Valid input")
# else:
#     print("Invalid input")

# ran = input("Choose a colour: ")
# if not ran == "Green":
#     print("Try again")

# ran = input("Choose the day of the week: ")
# if not ran == "Saturday":
#     print("It's not the weekend yet!")

# password="Again"
# ran = input("Insert the password here: ")
# if not password == ran:
#     print("Try again")

# b = input("Do you want a burger? ")
# f = input("Do you want fries? ")
# d = input("Do you want a drink? ")
# if b == "yes" and f == "yes" and not d == "yes":
#     print("Won't you get thirsty?")

# username = "John123"
# password = "pw123"
# uattempt = input("Whats the username: ")
# pattempt = input("Whats the password: ")
# if username == uattempt and password == pattempt:
#     print("Access Granted")
# elif username == uattempt or password == pattempt:
#     print("Either one is wrong")
# else:
#     print("Access Denied")

status = "Active" or "Paused"
if status == "Active" or "Paused":
    print("Game in progress ...")
else:
    print("Game is paused or inactive.")