# print("Hello from lesson 10")

# num = int(input("Choose a random number: "))
# if num >-1:
#     print(str(num) + " is positive")
# else:
#     print(str(num) + " is negative")

# import random
# num = random.randint(1,10)
# guess = int(input("Guess a random number from 1 to 10 : "))
# if guess == num:
#     print("Congratulations!! You did it!")
# else:
#     print("Oops, better luck next time!")

num1 = int(input("choose a number "))
if int(num1) % 2 == 0: #dont need convert here if u already converted above
    print("its even")
else:
    print("odd")