# print("Hello from lesson 13")

# balance = 1000
# while True:
#     print("1. Withdraw")
#     print("2. Deposit")
#     print("3. Check Balance")
#     print("4. Exit")
#     print("")
    
#     decision = int(input("Your chosen number: "))
#     print("")

#     if decision == 1:
#         amount = int(input("How much do you want to withdraw: "))

#         if amount <= balance:
#             balance -= amount
#             print("Success! Your remaining balance is " + str(balance))
#             print("")
#         else:
#             print("You are BROKE!!!")
#             print("")

#     elif decision == 2:
#         amount = int(input("How much money do you want to deposit: "))
#         balance += amount
#         print("Success! Your remaining balance is " + str(balance))
#         print("")

#     elif decision == 3:
#         print("Success! Your remaining balance is " + str(balance))
#         print("")

#     elif decision == 4:
#         break

# groceries = [
#     "Apples",
#     "Bread",
#     "Carrots",
#     "Dates",
#     "Eggs",
#     "Flour",
#     "Grapes",
#     "Honey"
# ]
# print(groceries)

# groceries = [
#     "Apples",
#     "Bread",
#     "Carrots",
#     "Dates",
#     "Eggs",
#     "Flour",
#     "Grapes",
#     "Honey"
# ]
# groceries[7] = "8. Herbs"

# print(groceries)

# groceries = [
#     "Apples",
#     "Bread",
#     "Carrots",
#     "Dates",
#     "Eggs",
#     "Flour",
#     "Grapes",
#     "Honey"
# ]
# groceries.append ("Ice")
# groceries.insert (1, "Bananas")

# print(groceries)

# groceries = [
#     "Apples",
#     "Bread",
#     "Carrots",
#     "Dates",
#     "Eggs",
#     "Flour",
#     "Grapes",
#     "Honey"
# ]
# groceries.pop(1)

# print(groceries)

groceries = [
    "Apples",
    "Bread",
    "Carrots",
    "Dates",
    "Eggs",
    "Flour",
    "Grapes",
    "Honey"
]
for i in groceries:

    if i == "Apples":
        print(i + ": I need 5 of these")

    if i == "Carrots":
        print(i + ": I need 3 of these")

    if i == "Grapes":
        print(i + ": Get the FarmFresh ")

    else:
        print (i)