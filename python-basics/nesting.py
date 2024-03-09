# Nesting

tvShow = input("What's your favorite tv show?")
print()
if tvShow == "peppa pig":
    print("Ugh, why?")
    faveCharacter = input("Who's your favorite character?")
    if faveCharacter == "daddy pig":
        print("Right answer")
    else:
        print("Nah, Daddy Pig's the greatest")
elif tvShow == "paw patrol":
    print("Aww, sad times")
else:
    print("Yeah, that's cool and all...")