#from my_module import * 
from my_module import find_index as fi, text
import sys
courses = ['History', 'Math', 'Physics', 'Compsci']
index = fi(courses, 'Math')
print(index)
print(text)

print(sys.path)  #directories get added into the sys 


"""
The Sys module in python provides access to variables and functions
that interact closely with the python interpreter.
It is a built-in module.
It can retrieve system-specific information.

We can add our module to standard library.
"""
