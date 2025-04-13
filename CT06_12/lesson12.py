# print("Hello from lesson 12")

# ##########
# #Best code ever!!!#
# import time
# a = 0
# while True:
#     print(str(a))
#     a = a + 1
#     time.sleep(1)
# #Best code ever!!!#
# ##########

# num = int(input("Choose a random number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print ("The number is divisible by 3 and 5!")
# else:
#     print ("The number is not divisible by 3 and 5!")

# vis = 0
# i = int(input("what is the limit"))
# while vis < i:
#     vis += 1
#     print (vis)

# vis2 = 18
# i = int(input("what is the limit"))
# while vis2 < i:
#     vis2 += 1
#     print (vis2)

# vis3 = 4
# i = int(input("what is the limit"))
# while vis3 < i:
#     vis3 += 1
#     print (vis3)

# vis = 0
# while True:
#     inp = input("Add 1 visitor?")
#     if inp == "yes":
#         vis += 1
#         print(vis)
#     if vis == 3:
#         break

# print("Come another day")

# order = ""
# skip = True
# while True:
#     item = input("What is your order: ")
#     if item == "end":
#         break
#     else:
#         if skip == True:
#             order += item
#             skip = False
#         else:
#             order += " , " + item
# print (order)

# count = 10

# while count > 0:
#     print(count)
#     count -= 1
#     if count == 5 :
#         break
# else:
#     print("Happy New Year!")

import random
num1 = random.randint(1,10)
num2 = random.randint(1,10)
print("What is " + str(num1) + "+ " + str(num2) + "? ")
sum = num1 + num2