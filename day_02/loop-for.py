languages = ['Swift', 'Python', 'Go', 'JavaScript']

# run a loop for each item of the list
for language in languages:
    print(language)


# use of range() to define a range of values
values = range(4)

# iterate from i = 0 to i = 3
for i in values:
    print(i)

# ----------------------------------------------------------
# It is not mandatory to use items of a sequence within a for loop. For example,
languages = ['Swift', 'Python', 'Go']

for language in languages:
    print('Hello')
    print('Hi')

# ----------------------------------------------------------
# If we do not intend to use items of a sequence within the loop, we can write the loop like this:
languages = ['Swift', 'Python', 'Go']

for _ in languages:
    print('Hello')
    print('Hi')

# ----------------------------------------------------------
# for loop with else
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

# ----------------------------------------------------------

# ----------------------------------------------------------

# ----------------------------------------------------------
