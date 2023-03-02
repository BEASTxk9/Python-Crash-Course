# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 # run python3 tuples_sets.py(python3 "File Name.py") in terminal to display the output


# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))


# Single value needs trailing comma
# fruits2 = ('Apples') # <-- This will not display the string apples and the type when called without a trailing comma
fruits2 = ('Apples',)

# print(fruits, type(fruits2))
# print(fruits2, type(fruits2))

#  Get value
# print(fruits[1])

# Cant change value if it is a tuple
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# will give you an error saying its not defined because it was deleted
# print(fruits2)

#Get length
print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

#  Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

#  Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Add duplicate(does nothing because it already exists)
fruits_set.add('Apples')


# Clear set
# fruits_set.clear()

#  Delete set
# del fruits_set

print(fruits_set)