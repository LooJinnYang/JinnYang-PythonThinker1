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

# days = int(input("How many days have you borrowed this book? "))
# if days>25:
#     print("Remember to return your book!")
# else:
#     num = 25 - days
#     print("remember to return in " + str(num) + " days!")

# import random
# num = random.randint(1,10)
# guess = int(input("guess a number from 1 to 10: "))
# if num == guess:
#     print("Thats the magic number!")
# else:
#     print("Nope")

# num_apples = int(input("How many apples do you want to buy? "))
# if num_apples > 10:
#     print ("You will get a 10% discount for buying that many apples!")
#     price = num_apples * 0.90
#     print("the price of the " + str(num_apples) + " apples = $" + str(price))
# else:
#     price = num_apples * 1
#     print("the price of the " + str(num_apples) + " apples = $" + str(price))

# num_apples = int(input("How many apples do you want to buy? "))
# num_oranges = int(input("How many oranges do you want to buy? "))
# if num_apples > 5:
#     price = num_apples * 0.54
#     print("the price of the " + str(num_apples) + " apples = $" + str(price))
# else:
#     price = num_apples * 0.60
#     print("the price of the " + str(num_apples) + " apples = $" + str(price))
# if num_oranges > 5:
#     price2 = num_oranges * 0.81
#     print("the price of the " + str(num_oranges) + " oranges = $" + str(price2))
# else:
#     price2 = num_oranges * 0.90
#     print("the price of the " + str(num_oranges) + " oranges = $" + str(price2))
# total_price = float(price) + float(price2)
# total_price = float(f"{total_price:.1f}")
# print(total_price)

# positive_days = 0
# for i in range(7):
#     temp = int(input("What is today's temperature: "))
#     if temp > 30:
#         positive_days+=1
# print(str(positive_days))

sum=0
for i in range(7):
    savings= int(input("What is today's savings: "))