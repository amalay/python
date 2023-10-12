# -----------------------------------------------------------------
# Global variable, Local variable
# -----------------------------------------------------------------
global_var = 10

def my_function():    
    local_var = 20          # Define local variable
    
    global global_var
    global_var = 30         # Modify global variable value 

print(global_var)           # Print global variable value

# Call my_function function.
my_function()

print(global_var)           # Print the modified value of the global variable

# -----------------------------------------------------------------
# Global variable
# -----------------------------------------------------------------
num = 1 

def increament():
    num = num + 1

    print(num)

# Call increament function
increament()

# -----------------------------------------------------------------
# # Changing global variable from inside a function using global variable
# -----------------------------------------------------------------
num = 1 

def increament():    
    global num          # Use of global keyword

    num = num + 1

    print(num)

# Call increament function
increament()

# -----------------------------------------------------------------
# 
# -----------------------------------------------------------------
def outer():
    message = 'local'

    # Nested function  
    def inner():

        # Declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

# Call outer function
outer()

# -----------------------------------------------------------------
# 
# -----------------------------------------------------------------
def outer_function():
    num = 20

    def inner_function():
        global num
        num = 25
    
    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)

# Call outer_function function
outer_function()
print("Outside both function: ", num)
