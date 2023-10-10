# -----------------------------------------------------------------
# Interger variables
# -----------------------------------------------------------------
num = 1
print(num)    # Prints: 1
print(type(num))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Decimal variables
# -----------------------------------------------------------------
num = 2.5
print(num)    # Prints: 2.5
print(type(num))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Character variables
# -----------------------------------------------------------------
ch = 'a'
print(ch)    # Prints: a
print(type(ch))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# String variables
# -----------------------------------------------------------------
str = "Amalay Verma"
print(str)    # Prints: Amalay Verma
print(type(str))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Tuple variables
# -----------------------------------------------------------------
person = ('Amalay', 'Verma', 43) # Create a tuple 
print(person[0])   # Access element at index 0. Print: Amalay
print(person[1])   # Access element at index 1. Print: Verma
print(person[2])   # Access element at index 1. Print: 43
print(type(person))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Set variables
# -----------------------------------------------------------------
student_id = {112, 114, 116, 118, 115}  # Create a set named student_id
print(student_id)
print(type(student_id))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Dictionary variables
# -----------------------------------------------------------------
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'} # Create a dictionary named capital_city
print(capital_city)
print(type(capital_city))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Assigning multiple values to multiple variables at once.
# -----------------------------------------------------------------
a, b, c = 5, 3.2, 'Hello'
print(a)  # Prints: 5
print(b)  # Prints: 3.2
print(c)  # Prints: Hello 
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Assign the same value to multiple variables at once
# -----------------------------------------------------------------
site1 = site2  = 'https://amalayverma.com'
print(site1)  # Prints: https://amalayverma.com
print(site2)  # Prints: https://amalayverma.com
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Python is case-sensitive. So num and Num are two different variables.
# -----------------------------------------------------------------
num = 5 
Num = 55
print(num) # Prints: 5
print(Num) # Prints: 55
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Data Types.
# -----------------------------------------------------------------
num_1 = 5
print("Value:", num_1)  # Prints: 5
print("Data Type:", type(num_1))
print("\n-----------------------------------------------------------------")

num_2 = 2.0
print("Value:", num_2)  # Prints: 2.0
print("Data Type:", type(num_2))
print("\n-----------------------------------------------------------------")

num_3 = 1 + 2j
print("Value:", num_3)  # Prints: 
print("Data Type:", type(num_3))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Data Types Casting.
# -----------------------------------------------------------------
num_int = 123
num_float = 1.23
num_result = num_int + num_float
print("Value:", num_result)  # Prints: 
print("Data Type:", type(num_result))
print("\n-----------------------------------------------------------------")

num_string = '12'
num_integer = 23
print("Data type of num_string before Type Casting:", type(num_string))

# Explicit type conversion
num_string = int(num_string)
print("Data type of num_string after Type Casting:", type(num_string))

num_result = num_integer + num_string
print("Value:", num_result)
print("Data Type:", type(num_result))