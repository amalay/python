def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')

# ---------------------------------------
# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ",sum)

# function call with two values
add_numbers(5, 4)

# Output: Sum: 9

# -----------------------------------------------
# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)

print('Square:',square)

# Output: Square: 9

# ------------------------------------------
# function that adds two numbers
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

# calling function with two values
result = add_numbers(5, 4)

print('Sum: ', result)

# Output: Sum: 9

# ---------------------------------------
import math

# sqrt computes the square root
square_root = math.sqrt(4)

print("Square Root of 4 is",square_root)

# pow() comptes the power
power = pow(2, 3)

print("2 to the power 3 is",power)

# --------------------------------------------
# function definition
def get_square(num):
    return num * num

for i in [1,2,3]:
    # function call
    result = get_square(i)
    print('Square of',i, '=',result)

# ------------------------------------
def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)


# function call with two arguments
add_numbers(2, 3)

#  function call with one argument
add_numbers(a = 2)

# function call with no arguments
add_numbers()

# -------------------------------------------
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name = 'Cartman', first_name = 'Eric')

# ---------------------------------------------
# program to find sum of multiple numbers 

def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)

# ----------------------------------------
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))

# --------------------------------------------
# Lambda/Anonymous Function
# declare a lambda function
greet = lambda : print('Hello World')

# call lambda function
greet()

# Output: Hello World

# -------------------------------------------
# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name)

# lambda call
greet_user('Delilah')

# Output: Hey there, Delilah

# ----------------------------------------------
# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()

# --------------------------------------
# global variable
c = 1 

def add():

     # increment c by 2
    c = c + 2

    print(c)

add()

# ------------------------------------------
# Changing Global Variable From Inside a Function using global
# global variable
c = 1 

def add():

    # use of global keyword
    global c

    # increment c by 2
    c = c + 2 

    print(c)

add()

# Output: 3 

# --------------------------------------
def outer_function():
    num = 20

    def inner_function():
        global num
        num = 25
    
    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)

outer_function()
print("Outside both function: ", num)

