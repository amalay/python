# -----------------------------------------------------------------
# Concatenation
# -----------------------------------------------------------------
str_1 = 'Amalay'
str_2 = 'Verma'
result = str_1 + str_2;

print('Concatenation of {} and {} is: {}'.format(str_1, str_2, result))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Addition
# -----------------------------------------------------------------
num_1 = 7
num_2 = 2
result = num_1 + num_2;

print('Addition of {} and {} is: {}'.format(num_1, num_2, result))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Subtraction
# -----------------------------------------------------------------
num_1 = 7
num_2 = 2
result = num_1 - num_2;

print('Subtraction of {} and {} is: {}'.format(num_1, num_2, result))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Multiplication
# -----------------------------------------------------------------
num_1 = 7
num_2 = 2
result = num_1 * num_2;

print('Multiplication of {} and {} is: {}'.format(num_1, num_2, result))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Division
# -----------------------------------------------------------------
num_1 = 7
num_2 = 2
result = num_1 / num_2;

print('Division of {} and {} is: {}'.format(num_1, num_2, result))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Floor Division
# -----------------------------------------------------------------
num_1 = 7
num_2 = 2
result = num_1 // num_2;

print('Floor division of {} and {} is: {}'.format(num_1, num_2, result))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Modulo Division
# -----------------------------------------------------------------
num_1 = 7
num_2 = 2
result = num_1 % num_2;

print('Modulo division of {} and {} is: {}'.format(num_1, num_2, result))
print("\n-----------------------------------------------------------------")
 
# -----------------------------------------------------------------
# Power (Ex. a to the power b)
# -----------------------------------------------------------------
num_1 = 7
num_2 = 2
result = num_1 ** num_2;

print('{} to the power {} is: {}'.format(num_1, num_2, result))
print("\n-----------------------------------------------------------------")
  
# -----------------------------------------------------------------
# Logical AND
# -----------------------------------------------------------------
num_1 = 3
num_2 = 5
result = ((num_1 > 2) and (num_2 <= 5));

print('{} > 2 and {} <= 5: {}'.format(num_1, num_2, result))
print("\n-----------------------------------------------------------------")

result = (True and True)
print('{} and {}: {}'.format(True, True, result))

result = (True and False)
print('{} and {}: {}'.format(True, False, result))

result = (False and False)
print('{} and {}: {}'.format(False, False, result))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Logical OR
# -----------------------------------------------------------------
result = (True or True)
print('{} or {}: {}'.format(True, True, result))

result = (True or False)
print('{} or {}: {}'.format(True, False, result))

result = (False or False)
print('{} or {}: {}'.format(False, False, result))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Logical NOT
# -----------------------------------------------------------------
result = (not True)
print('not {}: {}'.format(True, result))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# 
# -----------------------------------------------------------------
x1 = 5
y1 = 5

x2 = 'Hello'
y2 = 'Hello'

x3 = [1, 2, 3]
y3 = [1, 2, 3]

result = (x1 is not y1)
print('Result:', result)    # Prints False
 
result = (x2 is y2)
print('Result:', result)    # Prints True

result = (x3 is y3)
print('Result:', result)    # Prints False
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# 
# -----------------------------------------------------------------
x = 'Hello world'
y = {1: 'a', 2: 'b'}

result = ('H' in x)         # Check if 'H' is present in x string
print('Result:', result)    # Prints True

result = ('hello' not in x) # Check if 'hello' is present in x string
print('Result:', result)    # Prints True

result = (1 in y)           # Check if 1 key is present in y
print('Result:', result)    # Prints True

result = ('a' in y)         # Check if 'a' key is present in y
print('Result:', result)    # Prints False
print("\n-----------------------------------------------------------------")