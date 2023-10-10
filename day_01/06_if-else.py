# -----------------------------------------------------------------
# If condition.
# -----------------------------------------------------------------
number = 10

if number > 0:  # Check if number is greater than 0
    print('Number is positive.')

print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# If & Else condition.
# -----------------------------------------------------------------
number = 10

if number > 0:
    print('Number is positive.')
else:
    print('Number is negative.')

print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# If, Elseif and Else condition.
# -----------------------------------------------------------------
number = 0

if number > 0:
    print("Number is positive.")
elif number == 0:
    print('Number is zero.')
else:
    print('Number is negative.')

print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Nesting of If, Else condition.
# -----------------------------------------------------------------
number = 5

if (number >= 0):    
    if number == 0:
      print('Number is zero.')    
    else:
        print('Number is positive.')
else:
    print('Number is negative.')

print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Check ODD or EVEN Number
# -----------------------------------------------------------------
number = int(input('Enter a number: '))

if number % 2 == 0:
    print('Number is even.')    
else:
    print('Number is odd.')