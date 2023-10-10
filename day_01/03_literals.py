# -----------------------------------------------------------------
# Numeric literal
# -----------------------------------------------------------------
PI = 3.14
GRAVITY = 9.8

# -----------------------------------------------------------------
# Boolean literal
# -----------------------------------------------------------------
status = True   # True or False

# -----------------------------------------------------------------
# Null literal
# -----------------------------------------------------------------
value = None

# -----------------------------------------------------------------
# Character literal
# -----------------------------------------------------------------
some_character = 'S'

# -----------------------------------------------------------------
# String literal
# -----------------------------------------------------------------
site_name = 'amalayverma.com'
some_string = 'Python is fun' 
seperator = "-----------------------------------------------------------------"
newline = "\n"

# -----------------------------------------------------------------
# List literal
# -----------------------------------------------------------------
fruits = ["apple", "mango", "orange"] 
print(fruits)

# -----------------------------------------------------------------
# Tuple literal
# -----------------------------------------------------------------
numbers = (1, 2, 3) 
print(numbers)

# -----------------------------------------------------------------
# Dictionary literal
# -----------------------------------------------------------------
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
print(alphabets)

# -----------------------------------------------------------------
# Set literal
# -----------------------------------------------------------------
vowels = {'a', 'e', 'i' , 'o', 'u'} 
print(vowels)

# -----------------------------------------------------------------
# import constant file which we have created earlier
# -----------------------------------------------------------------
print(seperator)
import constant

print(constant.PI) # prints 3.14
print(constant.GRAVITY) # prints 9.8
print(constant.site_name) # prints 3.14
print()