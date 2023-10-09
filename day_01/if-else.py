number = 10

# check if number is greater than 0
if number > 0:
    print('Number is positive.')

print('The if statement is easy')

# ---------------------------------
number = 10

if number > 0:
    print('Positive number')

else:
    print('Negative number')

print('This statement is always executed')

# ----------------------------------------
number = 0

if number > 0:
    print("Positive number")

elif number == 0:
    print('Zero')
else:
    print('Negative number')

print('This statement is always executed')

# -----------------------------------------
number = 5

# outer if statement
if (number >= 0):
    # inner if statement
    if number == 0:
      print('Number is 0')
    
    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')

# Output: Number is positive

