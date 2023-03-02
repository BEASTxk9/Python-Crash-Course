# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict
person = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'age' : 30
}

# Use constructor
# person2 = dict(first_name= 'Sara', last_name='Williams')

# Get value
# print(person['first_name'])
# print(person.get('last_name'))

# print(person, type(person))
# print(person2, type(person2))

# Add key/value
person['phone'] = '555-555-555'
# print(person)


# Get dict keys
# print(person.keys())

# Get dict items
# print(person.items())


# Copy dict
person2 = person.copy()
person2['city']= 'Boston'

# print(person2)

# Remove item
del(person['age'])
# OR POP
person.pop('phone')

# Clear
person.clear()

# Get length
# print(len(person2))

# print(person)

# List of dict
people = [
    {'name': 'Martha', 'age':30},
    {'name': 'Kevin', 'age':25}
]

print(people)
print(people[1]['name'])