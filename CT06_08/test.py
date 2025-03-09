# #ask for name and assign to variable
# name=input("What is your name? ")
# #print out the name with additional string
# print("Nice to meet you, " + name)

#asking the user for inputs for the range function
start=int(input("What is your selected start number? "))
stop=int(input("What is your selected stop number? "))
increment=int(input("What is your selected increment number? "))

#
for i in range(start, stop, increment):
    print(i)