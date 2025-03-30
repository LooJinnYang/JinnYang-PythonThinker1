# print("Hello from lesson 10")

# num = int(input("Choose a random number: "))
# if num >-1:
#     print(str(num) + " is positive")
# else:
#     print(str(num) + " is negative")

import random
num = random.randint(10)
guess = int(input("Guess a random number from 1 to 10 : "))
if guess == num:
    print("")
