# print("Hello from lesson 9")

# import random
# num1 = random.randint(1,6)
# num2 = random.randint(1,6)
# num3 = random.randint(1,6)
# print("1st number: " + str(num1))
# print("2nd number: " + str(num2))
# print("3rd number: " + str(num3))
# num11 = int(num1) % 2 == 0
# num22 = int(num2) % 2 == 0
# num33 = int(num3) % 2 == 0
# all_even_odd = num11 == num22 == num33
# print(all_even_odd)

days = int(input("How many days have you borrowed this book? "))
if days>25:
    print("Remember to return your book!")
else:
    num = 25 - days
    print("remember to return in " + str(num) + "")

# import random
# num = random.randint(1,10)
# guess = int(input("guess a number from 1 to 10: "))
# if num == guess:
#     print("Thats the magic number!")
# else:
#     print("Nope")