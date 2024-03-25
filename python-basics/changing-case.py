#CASE:
# Changing case in a string with methods
# title() -> This method changes each word to title case

name = "ada lovelace"
print(name.title()) # Ada Lovelace

# upper() -> This method changes every word to uppercase
print(name.upper()) # ADA LOVELACE

# lower() -> This method changes every word to lowercase
print(name.lower()) # ada lovelace

'''
The lower() method is particularly useful for storing data. You typically
won’t want to trust the capitalization that your users provide, so you’ll
convert strings to lowercase before storing them. Then when you want to
display the information, you’ll use the case that makes the most sense for
each string.
'''