# Using Tabs or Newlines to create whitespace

# Using tab -> \t:
print("Python")
print("\tPython")

# Adding a newline
print("Languages:\nPython\nC\nJavaScript")

# Combining newlines and tabs
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping Whitespace

# rstrip() -> removes whitespace on the right
favorite_language = 'python ' # Length of 7
favorite_language.rstrip() # Length of 6

# lstrip() -> removes whitespace on the left
favorite_language = ' python' # Length of 7
favorite_language.lstrip() # Length of 6

# strip() -> removes whitespace on both sides
favorite_language = ' python ' # Length of 8
favorite_language.strip() # Length of 6
