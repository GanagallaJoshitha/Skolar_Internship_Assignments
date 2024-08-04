######Lists###################




# Creating a list
my_list = [1, 2, 3, 4, 5]

# Appending to the list
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Inserting into the list
my_list.insert(3, 'a')
print(my_list)  # Output: [1, 2, 3, 'a', 4, 5, 6]

# Removing from the list
my_list.remove('a')
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Popping from the list
popped_item = my_list.pop()
print(popped_item)  # Output: 6
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Sorting the list
my_list.sort(reverse=True)
print(my_list)  # Output: [5, 4, 3, 2, 1]


######Functions###################


# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# Function with default parameter
def add(a, b=5):
    return a + b

print(add(3))      # Output: 8
print(add(3, 7))   # Output: 10

# Function with variable-length arguments
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))  # Output: 24

# Function with keyword arguments
def describe_person(name, **attributes):
    description = f"Person: {name}\n"
    for key, value in attributes.items():
        description += f"{key}: {value}\n"
    return description

print(describe_person("John", age=30, occupation="Engineer"))

#########Python Module################

# Importing an entire module
import math
print(math.sqrt(16))  # Output: 4.0

# Importing specific functions
from math import pi, sin
print(pi)  # Output: 3.141592653589793
print(sin(pi/2))  # Output: 1.0

# Renaming a module
import math as m
print(m.factorial(5))  # Output: 120

# Creating a custom module (save this in a file named my_module.py)
# my_module.py
def custom_function(x):
    return x * x

# Using the custom module
import my_module
print(my_module.custom_function(4))  # Output: 16

