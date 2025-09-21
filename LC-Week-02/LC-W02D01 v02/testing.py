import os
import sys

# This is a comment! Python will ignore it.

"""
This is a
multiline comment
"""

total_guitars = 7  # Hope someone knows how to play guitar

print("10:",total_guitars)
total_guitars = 8
print("12:",total_guitars)

my_number = 15

# illegal syntax...
# my_variable

num1=42
str1='hello'
str2="world"
bool1=True
print(num1,type(num1))
# class 'int'>
print(str1,type(str1))
print(str1,type(str2))
# class 'str'>
print(bool1,type(bool1))
# class 'bool'>
# 
some_int = 25.0
print(some_int,type(some_int))



def clear_console():
    """
    Clears the console screen based on the operating system.
    """
    if sys.platform.startswith('win'):
        # For Windows
        os.system('cls')
    else:
        # For Linux, macOS, or other Unix-like systems
        os.system('clear')


clear_console()


a_float = 1.23
an_int = int(a_float)

print(a_float,type(a_float))
print(an_int,type(an_int))


z = 3.14 + 2.71j - 2.04 - 1.01j
print(z,type(z))

my_nothing = None

print(my_nothing,type(my_nothing))

quotient1 = 5 // 2
quotient2 = 5 / 2

print(quotient1)
print(quotient2)
