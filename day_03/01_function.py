# -----------------------------------------------------------------
# Define simple function
# -----------------------------------------------------------------
def Hello():
    return 'Hello World!'

# -----------------------------------------------------------------
# Define add function with two arguments
# -----------------------------------------------------------------
def add(num_1, num_2):
    return num_1 + num_2

# -----------------------------------------------------------------
# Define square function.
# -----------------------------------------------------------------
def square(num):
    return num * num

# import math
# square_root = math.sqrt(4)
# power = pow(2, 3)

# -----------------------------------------------------------------
# Define add function to calculate sum of multiple numbers.
# -----------------------------------------------------------------
def add(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    return result

# Call add function with 3 arguments
# add(1, 2, 3)

# Call add function with 2 arguments
# add(4, 9)

# -----------------------------------------------------------------
# Define factorial function.
# -----------------------------------------------------------------
def factorial(num):
    """This is a recursive function to find the factorial of an integer"""

    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))

# Call factorial function
# factorial(3)

# -----------------------------------------------------------------
# Define Lambda/Anonymous function.
# -----------------------------------------------------------------
welcome = lambda : print('Welcome!')

# Call lambda function
# welcome()

# -----------------------------------------------------------------
# Define Lambda/Anonymous function with one argument.
# -----------------------------------------------------------------
welcome = lambda name : print('Welcome!', name)

# Call lambda function with one argument
# welcome('Amalay')