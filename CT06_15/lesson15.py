# print("Hello from lesson 15")

# counter = 0

# def increment_counter():
#     global counter
#     counter += 1

# for i in range(3):
#     increment_counter()

# print(counter)

# # Task 7: Even or Odd? III
# # Create a function that takes in a number and returns whether it is
# # even

# # 1. Create a function named isEven()
# def is_Even(num):

# # 2. If the number is even, the function should return True
# # 3. If the number is odd, the function should return False
#     return num % 2 == 0

# # 4. Using the 'isEven()' function, loop through a list of numbers and
# #    print them out in this format:
# #     "3 is an odd number"
# #     "9 is an odd number"
# #     "2 is an even number"

# nums = [3,5,8,326,4,]

# for num in (nums):
#     if is_Even(num):
#         print(str(num) + " is an even number.")
#     else:
#         print(str(num) + " is an odd number.")

# *Troll code* ##########################

# num = [1,2,3,4,6,7,8]
# for num in (num):
#     num % 2 == 0
#     if num == True:
#         print(str(num) + " is an even number.")
#     else:
#         print(str(num) + " is an odd number.")

##########################################


def square(num):
    return num * num

def square_of_sum(num1,num2):
    return square(num1) + square(num2)


inp1 = int(input("First number: "))
inp2 = int(input("Second number: "))
print(square_of_sum(inp1,inp2))