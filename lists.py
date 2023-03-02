# A List is a collection which is ordered and changeable. Allows duplicate members.

# run python3 lists.py(python3 "File Name.py") in terminal to display the output


# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges','Grapes', 'Pears']

# Use a constructor
# number2 = list((1, 2, 3, 4, 5))

# output
# print(numbers, number2)

# Get a value
print(fruits[1].capitalize())

# Get length
print(len(fruits))

# Append to list(add)
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Insert into position (object postion in array/list, 'replacement value')
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort List
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)