# print("Hello from lesson 15")

counter = 0

def increment_counter():
    global counter
    counter += 1

for i in range(3):
    increment_counter()

print(counter)



num = input("Choose a number to double")