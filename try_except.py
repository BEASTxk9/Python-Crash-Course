# Try and Except is used inorder to stop errors that might stop the flow of the code
# Basically Error handling

# Example
num = 'one'

try:
    
    # this will cause an error because you cannot turn a str of words to an int
    num = int(num)
    
except:
    # this will prevent an error allowing the code to continue runing
    num = 'undefined(Error)'
    
print(f'First query: {num}')


# ________________________________________
num2 = '2'
try:
    # this will run because you can turn a str of numbers to an int/float
    num2 = int(num2)
    
except:
    num2 = 'undefined(Error)'
    
print(f'Second query: {num2}')