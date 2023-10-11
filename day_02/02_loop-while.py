import constant

# -----------------------------------------------------------------
# Programm to print numbers from 1 to 5
# -----------------------------------------------------------------
i = 1
n = 5

while i <= n:
    print(i)
    i = i + 1

print(constant.SEPERATOR)

# -----------------------------------------------------------------
# Program to calculate the sum of numbers until the user enters zero
# -----------------------------------------------------------------
total = 0

number = int(input('Enter a number: '))

while number != 0:          
    total = total + number      # Add numbers until number is zero        
    number = int(input('Enter a number: '))     # Take input again
    
print('Total =', total)
print(constant.SEPERATOR)

# -----------------------------------------------------------------
# Programm to test condition which is always True
# -----------------------------------------------------------------
age = 32

while age > 18:
    print('You can vote')

print(constant.SEPERATOR)

# -----------------------------------------------------------------
# While loop with else
# -----------------------------------------------------------------
counter = 0

while counter < 3:
    print('Inside while loop.')
    counter = counter + 1
else:
    print('Inside else condition.')

print(constant.SEPERATOR)

# -----------------------------------------------------------------
# While loop with break and else
# -----------------------------------------------------------------
counter = 0

while counter < 3:    
    if counter == 1:    # Loop ends because of break the else part is not executed 
        break

    print('Inside while loop.')
    counter = counter + 1
else:
    print('Inside else condition.')

print(constant.SEPERATOR)
