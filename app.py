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