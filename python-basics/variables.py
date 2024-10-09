# NAMING REQUIREMENTS
# ---------------------------
# Variables in Python are required to start with a letter or an underscore.
# The rest of the name must consist of letters, numbers, or underscores
# Names are case-sensitive

_cats = "meow"
abc123 = 1970

# NAMING CONVENTIONS
# --------------------------
# Most variable names should be written in lower_snake_case. This means that all words should be lowercase, and words should be separated by an underscore.
# CAPITAL_SNAKE_CASE usually refers to constants
# UpperCamelCase usually refers to a class (more on that later)
# Variables that start and end with two underscores (called “dunder” for double underscore) are intended to be private or are builtins to the language

myVariable = 3  # Get outta here, this isn't JavaScript!
my_variable = 3  # much better
AVOGADRO_CONSTANT = 6.022140857 * 10 ** 23
__no_touchy__ = 3  # someone doesn't want you to mess with this!

# DYNAMIC TYPING
# Python is highly flexible about assigning and reassigning variables to any type at any time:

awesomeness = None
awesomeness = 33.5
awesomeness = True

# However, Python is NOT weakly or “loosely”-typed; it is a strongly-typed language. That means that while variables can be dynamically reassigned to different types, you cannot implicitly convert variables between types

# This is a contrast from JavaScript, which is weakly-typed (type coercion)

