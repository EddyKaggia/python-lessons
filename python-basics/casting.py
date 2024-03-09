# Casting -> Converting strings to integers/ floats
# Int -> whole number
# Float -> Has decimal

myScore = int(input("Your score: "))
print()
if myScore > 100000:
    print("Winner!")
else:
    print("Try again \U0001F622")
print()
print()

myPi = float(input("What is pi to 3dp? "))
print()
if myPi == 3.142:
    print("Correct!")
else:
    print("Try again \U0001F622")