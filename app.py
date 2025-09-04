#Comments
#Comment can be added using

print('hello') # This is a comment

"""
 This is the comment 
 written in 
 multiple lines 
"""
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

"""
Now lets go through the variables

Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

In Python, you cannot use a variable without assigning it a value first.
"""
a = 'manoj' # This is of type str
x = 1 # This is type int
y = 2

print(x+y)

# Casting

x = str('3') # Here x = '3'
y = int(3) # Here y = 3
z = float('3') # Here z = 3.0

# Here is how we can get the type od the variable

xx ='John'

print(type(xx))

# String variables can be declared using single and double quotes both has same meaning.

e = 'manoj'
# Both are same
e = "manoj"

# Python is case-sensitive.

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

"""
Rules for Python variables:
    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
    A variable name cannot be any of the Python keywords.
"""

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# Assigning multiple values

g,h,j = 'manoj', 'naik', 'ravi';
print(g)
print(h)
print(j)

g=h=j = 'Orange' # all will print same value
print(g)
print(h)
print(j)

# Unpack a collection

fruits = ['apple', 'banana', 'orange']
c,v,b = fruits
print(c) # apple
print(v) #banana
print(b) # orange

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# Output variables
# The Python print() function is often used to output variables.

x = 'python'
y = 'is'
z = 'awesome'

print(x,y,z) # Output > python is awesome


x = 'python'
y = 'is'
z = 'awesome'

print(x+y+z) # Output > python is awesome
# For numbers '+' works as a mathematical operator

x=5
y='john'
print(x+y) # produces Error TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Best way to print the above code is
print(x,y)

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# Global variable

"""
The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
"""

# Example
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# we cannot change the global variable value inside the function. To change we need to use the keyworrd global.
# Example

x = 100
def func():
    global x
    x = 50
func()
print(x)

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------


# Python Data Types

"""
    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray
    None Type:	NoneType
"""
# Setting a specific data type in python

x = str('s') # Specifies str data type
x= list(('apple', 'banana', 'orange'))
x= tuple(('apple', 'banana', 'orange'))
x = dict(name='manoj', age=30)
x = set(('apple', 'banana', 'orange'))
x = frozenset(('apple', 'banana', 'orange'))
x= bool(5)

# --------------------------------------------------------------------------------# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------# --------------------------------------------------------------------------------

# Number

"""
    int 
    flot 
    complex
"""

x = 1    # int
y = 2.8  # Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
z = 1j   # complex here j is an imaginary number

# Type conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x) # output > 1+0j

# Random number
import random

print (random.randrange(1,10))
print (random.randint(1,10))

# --------------------------------------------------------------------------------# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------# --------------------------------------------------------------------------------

# Casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# Strings

#Quotes inside quotes
print("It's alright") # It's alright
print("He is called 'Johnny'") # He is called 'Johnny'
print('He is called "Johnny"') # He is called "Johnny"

# multi line string
x = """
This is 
multi line 
comment
"""
# Both are same
x = '''
This is 
multi line 
comment
'''

# Strings are array, Like many other popular programming languages, strings in Python are arrays of unicode characters.
#  However, Python does not have a character data type, a single character is simply a string with a length of 1.
# This way we can access single element of the string.

a ="Hello, world!"
print(a[1]) # >

# looping through string

for x in 'banana':
    print(x)

# string length

d = 'apple'
print(len(d))

# check string
txt = "the best thing in life is for free."

print('free' in txt)

# using it in if statement

txt = "the best thing in life is for free."

if 'free' in txt:
    print('yes "free" in in the variable txt')

# checking if not

txt = "the best thing in life is for free."

print('ranger' not in txt)

# slicing string

# Get the characters from position 3, and all the way to the end:
b = 'hello world'
print(b[3:])

"""
Negative Indexing
    Use negative indexes to start the slice from the end of the string:
    Example
    Get the characters:
    
    From: "o" in "World!" (position -5)
    
    To, but not included: "d" in "World!" (position -2):
"""

b = 'hello world'
print(b[-5:-1])


x = 'Welcome'
print(x[3:5]) # output > co

"""
modify String 
.upper()
.lower() 
.strip() removes whitespaces
"""

# Replace
t = 'Hello, world'
print(t.replace('Hello', 'Hi'))

# Split string
t = 'Hello, world'
print(t.split(','))  # return ['Hello', ' world']

# String concatenation
a = "Hello"
b = "World"
c = a + b
print(c)  # prints HelloWorld

a = "Hello"
b = "World"
c = a + " " + b
print(c)   # prints Hello World

"""
Format strings
"""

age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt) # this will produce error

# Instead we can use format() or fstrings method

age = 36
txt = f"My name is John, I am {age}"
print(txt)

print(f'50 + 60 = {50+60}') # this will also work

"""
Escape Character
    To insert characters that are illegal in a string, use an escape character.
"""

txt = "We are the so-called "Vikings" from the north." # This will produce error

# But his will not
txt = "We are the so-called \"Vikings\" from the north."

# For single and double quotes we use single backslash '\'

# For backlash \\
# For New Line \n
# There are many other Escape characters like this

"""
String methods
There are many methods ref https://www.w3schools.com/python/python_strings_methods.asp
"""

# String format
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

#Python Booleans

print(10 > 9) #true
print(10 == 9) #false
print(10 < 9) #false

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

# Python Operators
    # Arithematic
    # assignment
    # comparision
    # logical identity
    # membership
    # bitwise

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

#Python Lists

# Accessing list item
x = ['a', 'b', 'c','d']
print(x[1]) #prints b

#Negative indexing
x = ['a', 'b', 'c','d']
print(x[-3: -1])  #dosent include 'd'
print(x[-1]) #prints d

# range of indexes
x = ['a', 'b', 'c','d']
print(x[1:3]) # prints bc dosent prints 'a'

# Range of negative indexes
x = ['a', 'b', 'c','d']
print(x[-3: -1 ]) # prints bc, dosent print 'd'

# Check is item exist
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")