# -----------------------------------------------------------------
# Input
# -----------------------------------------------------------------
# Syntax: input(prompt) ----> use input() to take user input

num = input('Enter a number: ')
print('Value:', num)
print('Data Type:', type(num))
print("\n-----------------------------------------------------------------")

num = int(input('Enter a number: '))
print('Value:', num)
print('Data Type:', type(num))
print("\n-----------------------------------------------------------------")

# -----------------------------------------------------------------
# Output
# -----------------------------------------------------------------
# Syntax: print(object= separator= end= file= flush=)

print('It is rainy today!')
print('Good Morning!', end= ' ')    # Print with end whitespace.
print('New Year', 2023, 'See you soon!', sep= '. ')
