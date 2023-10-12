# -----------------------------------------------------------------
# Global variable, Outer variable, Inner variable
# -----------------------------------------------------------------
global_var = 10             # global_var is in the global namespace

def outer_function():    
    outer_var = 20          #  outer_var is in the local namespace 

    def inner_function():        
        inner_var = 30      #  inner_var is in the nested local namespace 
        print(inner_var)

    print(outer_var)

    inner_function()

print(global_var)           # Print the value of the global variable

# Call the outer function.
outer_function()