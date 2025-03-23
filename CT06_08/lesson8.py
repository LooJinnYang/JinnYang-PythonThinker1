# print("Hello from lesson 8")

# import time
# for i in range(10,0,-1):
#     print(i)
#     time.sleep(1)
# print("Happy New Year")

# import time
# num = int(input("How many seconds to countdown from? "))
# for i in range(num,0,-1):
#     print(i)
#     time.sleep(1)
# print("Happy New Year")

# import random
# print(random.randint(1,6))

# import random
# for i in range(20):
#     print(random.randint(0,9999))

# import random
# for i in range(3):
#     print(random.randint(0,9999))

# x = True
# print (x)

# variable1 = True
# variable2 = True
# print (variable1 == variable2)

# variable1 = True
# variable2 = False
# print (variable1 == variable2)

# import random
# num1 = random.randint(1,50)
# num2 = random.randint(1,50)
# answer = int(input("What is " + str(num1) + " + " + str(num2) + " ? "))
# print(answer == (int(num1)+int(num2)))

# import random
# guess = int(input("guess a number from 1 to 10: "))
# num1 = random.randint(1,10)
# print(guess == num1)
# print("The actual number is " + str(num1))

# import random
# num = int(input("How many questions ?"))
# for i in range(num):
#     num1 = random.randint(1,10)
#     num2 = random.randint(1,10)
#     x = input("What is " + str(num1) + " x " + str(num2) + "? ")
#     print(int(x) == int(num1*num2))

import random

num1 = random.randint(1,6)
num2 = random.randint(1,6)
num3 = random.randint(1,6)

print("1st number: " + str(num1))
print("2nd number: " + str(num2))
print("3rd number: " + str(num3))

num11 = int(num1) % 2 == 0