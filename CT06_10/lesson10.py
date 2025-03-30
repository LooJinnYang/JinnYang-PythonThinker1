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

import random
num1 = random.randint(1,6)
num2 = random.randint(1,6)
num3 = random.randint(1,6)
print("1st number: " + str(num1))
print("2nd number: " + str(num2))
print("3rd number: " + str(num3))
num11 = int(num1) % 2 == 0
num22 = int(num2) % 2 == 0
num33 = int(num3) % 2 == 0
all_even_odd = num11 == num22 == num33
print(all_even_odd)