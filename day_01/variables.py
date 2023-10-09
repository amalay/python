seperator = "-----------------------------------------------------------------"
newline = "\n"

# -----------------------------------------------------------------
# Assigning multiple values to multiple variables
# -----------------------------------------------------------------
print(seperator)
a, b, c = 5, 3.2, 'Hello'

print(a)  # prints 5
print(b)  # prints 3.2
print(c)  # prints Hello 
print()

# -----------------------------------------------------------------
# Assign the same value to multiple variables at once
# -----------------------------------------------------------------
print(seperator)
site1 = site2  = 'amalayverma.com'

print(site1)  # prints amalayverma.com
print(site2)  # prints amalayverma.com
print()

# -----------------------------------------------------------------
# Python is case-sensitive. So num and Num are different variables
# -----------------------------------------------------------------
print(seperator)
num = 5 
Num = 55

print(num) # 5
print(Num) # 55
print()

# -----------------------------------------------------------------
# import constant file which we have created earlier
# -----------------------------------------------------------------
print(seperator)
import constant

print(constant.PI) # prints 3.14
print(constant.GRAVITY) # prints 9.8
print(constant.site_name) # prints 3.14
print()

num1 = 5
print(num1, 'is of type', type(num1))

num2 = 2.0
print(num2, 'is of type', type(num2))

num3 = 1+2j
print(num3, 'is of type', type(num3))

# create a tuple 
product = ('Microsoft', 'Xbox', 499.99)

# access element at index 0
print(product[0])   # Microsoft

# access element at index 1
print(product[1])   # Xbox

# create a set named student_id
student_id = {112, 114, 116, 118, 115}

# display student_id elements
print(student_id)

# display type of student_id
print(type(student_id))

# create a dictionary named capital_city
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}

print(capital_city)


# create a dictionary named capital_city
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}

print(capital_city)


integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))


num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))

# print(object= separator= end= file= flush=)

# print with end whitespace
print('Good Morning!', end= ' ')
print('It is rainy today')

print('New Year', 2023, 'See you soon!', sep= '. ')

print('Amalay is ' + 'awesome.')

x = 5
y = 10

print('The value of x is {} and y is {}'.format(x,y))

# input(prompt)
# using input() to take user input
num = input('Enter a number: ')
print('You Entered:', num)
print('Data type of num:', type(num))

num = int(input('Enter a number: '))