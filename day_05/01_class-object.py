import sys
import os

current_file_path = os.path.realpath(__file__)
current_dir = os.path.dirname(current_file_path)
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from constant import Messages
# =======================================================================

class Person:
    id = 0
    name = None
    age = 0

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def display(self):
        print('Person Details:')
        print('Id: ', self.id)
        print('Name: ', self.name)
        print('Age: ', self.age)
        print(Messages.SEPERATOR)

# -----------------------------------------------------------------
# Instantiation of Person class.
# -----------------------------------------------------------------
person = Person(1, 'Amalay', 43)
person.display()

# -----------------------------------------------------------------
# Instantiation of Person class with different information.
# -----------------------------------------------------------------
person = Person(2, 'Mahesh', 32)
person.display()

# -----------------------------------------------------------------
# List of instantiation of Person class.
# -----------------------------------------------------------------
persons = []

persons.append(Person(3, 'Mangat', 38))
persons.append(Person(4, 'Samik', 34))
persons.append(Person(5, 'Rakesh', 40))

for person in persons:
    person.display()

# -----------------------------------------------------------------
# List of instantiation of Person class.
# -----------------------------------------------------------------
persons = []

# Using list comprehension to append instances to persons
persons += [Person(id, name, age) for id, name, age in [(6, 'Akash', 25), (7, 'Deependra', 40), (8, 'Veer', 67)]]

for person in persons:
    person.display()