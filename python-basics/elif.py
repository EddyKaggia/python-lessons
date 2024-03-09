# Elif statements

print("SECURE LOGIN")
print()
username = input("Username > ")
password = input("Password > ")
print()
if username == "Drew" and password == "password":
    print("Welcome Drew!")
elif username == "Susan" and password == "password":
    print("Welcome Susan!")
else:
    print("You are trespassing!")