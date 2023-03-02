# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name= 'Brad'
age = 37

# run python3 strings.py(python3 "File Name.py") in terminal to display the output


# output method 1
# concatenate(insert variable into a string)
# print('Hello, my name is ' + name + 'and I am ' + str(age))


# String Formatting

# output method 2
# Arguments by position
# print('My name is {name} and I am {age}'. format(name=name, age=age))

# output method 3
# F-Strings (3.6+)
# print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'hello world'

# String functions

#Capitalize string 
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list/array
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

# if you remove the space between 'hello world' eg. 'helloworld' the string will become alphanumeric & alphabetic