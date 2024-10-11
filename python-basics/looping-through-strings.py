# STRINGS IN PYTHON
# ---------------------
# A Python string is an iterable series of characters. You can loop through a string just like a list:

for x in "word":
    print(x)
    
# Most importantly, strings in Python are immutable. This means you cannot change strings like so:

my_str = "can't touch this"
# my_str[6] = " "  # TypeError

new_str = "hello "
for c in "world":
    new_str += c  # new string created every single time!

print(new_str)  # hello world