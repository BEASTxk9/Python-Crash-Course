# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime
from datetime import date

import time
from time import time

# Pip module
# from camelcase import CamelCase

# import custon module from validator.py
import validator
from validator import validate_email


# today = datetime.date.today()
today = date.today()

# timestamp = time.time()
timestamp = time()


email = 'test@gmail.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')

print(today)
print(timestamp)

# C = CamelCase()
# print(c.hump('hello there world'))

# when installing python packages you would use pip/pip3
# run " pip3 --version " to check the version
# run " pip3 install camelcase " to install package 
# run " pip3 freeze " to check all modules/packages installed
# once you install a module/package you can import it