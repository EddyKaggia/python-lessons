# Nesting

tvShow = input("What's your favorite tv show?")
print()
if tvShow == "Invincible":
    print("It's a vibe")
    faveCharacter = input("Who's your favorite character?")
    if faveCharacter == "Mark":
        print("Right answer")
    else:
        print("Nah, Mark's the greatest")
elif tvShow == "paw patrol":
    print("Aww, sad times")
else:
    print("Yeah, that's cool and all...")