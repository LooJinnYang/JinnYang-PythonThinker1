# print("Hello from lesson 12")

num = int(input("Choose a random number: "))
if num % 3 == 0 and num % 5 == 0:
    print ("The number is divisible by 3 and 5!")
else:
    print ("The number is not divisible by 3 and 5!")

vis = 0
while vis < 50:
    vis = vis + 1
    print 