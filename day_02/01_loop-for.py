# import constant
from . import constant

# -----------------------------------------------------------------
# Run a loop for each item of the list.
# -----------------------------------------------------------------
languages = ['C#', 'Python', 'Go', 'JavaScript']

for language in languages:
    print(language)

print(constant.seperator)

# -----------------------------------------------------------------
# Use of range() to define a range of values
# -----------------------------------------------------------------
items = range(4)

for item in items:
    print(item)

print(constant.seperator)

# -----------------------------------------------------------------
# It is not mandatory to use items of a sequence within a for loop. For example:
# -----------------------------------------------------------------
languages = ['C#', 'Python', 'Go', 'JavaScript']

for language in languages:
    print('Hello')
    print('Hi')

print(constant.seperator)

# -----------------------------------------------------------------
# If we do not intend to use items of a sequence within the loop, we can write the loop like this:
# -----------------------------------------------------------------
languages = ['C#', 'Python', 'Go', 'JavaScript']

for _ in languages:
    print('Hello')
    print('Hi')

print(constant.seperator)

# -----------------------------------------------------------------
# For loop with else
# -----------------------------------------------------------------
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

print(constant.seperator)

# ----------------------------------------------------------

# ----------------------------------------------------------

# ----------------------------------------------------------
