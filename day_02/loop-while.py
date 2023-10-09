# program to display numbers from 1 to 5

# initialize the variable
i = 1
n = 5

# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1

# -----------------------------------------------------
# program to calculate the sum of numbers
# until the user enters zero

total = 0

number = int(input('Enter a number: '))

# add numbers until number is zero
while number != 0:
    total += number    # total = total + number
    
    # take integer input again
    number = int(input('Enter a number: '))
    

print('total =', total)

# ----------------------------------------
age = 32

# the test condition is always True
while age > 18:
    print('You can vote')

# --------------------------------
counter = 0

while counter < 3:
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')

#----------------------------------------
counter = 0

while counter < 3:
    # loop ends because of break
    # the else part is not executed 
    if counter == 1:
        break

    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')

    