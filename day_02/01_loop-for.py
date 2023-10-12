import constant

# -----------------------------------------------------------------
# Run a loop for each item of the list.
# -----------------------------------------------------------------
languages = ['C#', 'Python', 'Go', 'JavaScript']

for language in languages:
    print(language)

print(constant.SEPERATOR)

# -----------------------------------------------------------------
# Use of range() to define a range of values
# -----------------------------------------------------------------
items = range(4)

for item in items:
    print(item)

print(constant.SEPERATOR)

# -----------------------------------------------------------------
# It is not mandatory to use items of a sequence within a for loop. For example:
# -----------------------------------------------------------------
languages = ['C#', 'Python', 'Go', 'JavaScript']

for language in languages:
    print('Hello')
    print('Hi')

print(constant.SEPERATOR)

# -----------------------------------------------------------------
# If we do not intend to use items of a sequence within the loop, we can write the loop like this:
# -----------------------------------------------------------------
languages = ['C#', 'Python', 'Go', 'JavaScript']

for _ in languages:
    print('Hello')
    print('Hi')

print(constant.SEPERATOR)

# -----------------------------------------------------------------
# For loop with else
# -----------------------------------------------------------------
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

print(constant.SEPERATOR)

# -----------------------------------------------------------------
# Nested for loop
# -----------------------------------------------------------------
number = 5

for i in range(number):
    for j in range(number):        
        print('i = {}, j = {}, i * j = {}'.format(i, j, i * j))

    print(constant.SEPERATOR)

# ----------------------------------------------------------

# ----------------------------------------------------------
