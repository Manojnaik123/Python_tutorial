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

# Changing the list item
theList = ['apple', 'banana', 'cherry']
theList.insert(2, "watermelon") # output ['apple', 'banana', 'watermelon', 'cherry']

# append function - adds element to the last of the list
theList = ['apple', 'banana', 'cherry']
theList.append("watermelon")


# extend - joins the list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) # we can use any other iterable apart from the list like tuples sets, and dictionaries
print(thislist)

# remove item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") # removes banana from the list
print(thislist)

# if there are multiple element like banana below then remove will remove the first occurance

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) # prints ['apple', 'cherry', 'banana', 'kiwi']

# pop methof for remove

thislist.pop() # removes the last element

theList.pop(1) # removes the element at the index 1

# The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist

# clear function empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# List comprehension - shortening the for loop in a single line

thislist = ["apple", "banana", "cherry"]

newlist = [x for x in thislist] #-  ["apple", "banana", "cherry"]

newlist = [x for x in thislist if 'a' in x ] #-  ["apple", "banana"]

newlist = [x for x in range(10) if x < 5 ]

print(newlist) #- [0,1,2,3,4]


# Sorting

list1 = [1, 5, 3, 4, 2]

list1.sort() # by default ascending order
print(list1) # - [1,2,3,4,5]


list1 = [1, 5, 3, 4, 2]
list1.sort(reverse=True) # Sorts in reverse of the default that is reverse of asc
print(list1) # - [5,4,3,2,1]

# Case sensitive sorting

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # prints ['Kiwi', 'Orange', 'banana', 'cherry']

# to prevent this

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # - ['banana', 'cherry', 'Kiwi', 'Orange']


# Reverse - reverses the list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # - ['cherry', 'Kiwi', 'Orange', 'banana']


# copying a list

thislist = ["banana", "Orange", "Kiwi", "cherry"]

newlist = thislist.copy()
print(newlist)

# another method is to use list()

thislist = ["banana", "Orange", "Kiwi", "cherry"]

newlist = list(thislist)
print(newlist)

# We can also use the slice for copying the list
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# Joining two list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
list2 = [1,2,3,4]

# one of the easiest way is using + operator

# Example:

list3 = thislist + list2

# Another method is using the for loop

for x in list2:
    thislist.append(x)

# another method is using the extend function

thislist.extend(list2)

"""
These are all the list functions 

append() - adds the element to the last of the list 
clear() - Empties the list 
copy() - Returns a copy os the list 
count() - returns the number of time the element is present in the list, string, tuple and others
extend() - adds the elements of the list to the end of the current list
index() - returns the index of the first element with the specified value 
pop() - removes the last element, or we can also specify the index to remove the element 
remove() - removes the element with the specified value 
reverse() - reverses the list 
sort() - used to sort the list, we can also reverse it using the sort(reverse = true)
"""


"""
Tuple 
Tuple items are ordered, unchangeable, and allow duplicate values.
"""

# Creating tuple with one element

t = (1)
print(type(t))  # > Class int

t=(1,)
print(type(t)) # > tuple

# TUPLE constructor

thistuple = tuple(('apple', 1, 2))

# accessing tuple
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[1]) # prints second element

print(thistuple[-1]) # prints last element

print(thistuple[2:5]) # prints ('cherry', 'orange', 'kiwi')

print(thistuple[: 5]) # ("apple", "banana", "cherry", "orange", "kiwi")

print(thistuple[3:]) # ('orange', 'kiwi', 'melon', 'mango')

print(thistuple[-4:-2]) # ('orange', 'kiwi')# Checking is element exist in tuple.

if "apple" not in thistuple:
    print(True)

# Updating tuple

# changing the value of the element

t = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
x= list(t)
x[0] = 'hamster'
t= tuple(x)
print(t)

# adding value into the tuple

t = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
x= list(t)
x.append('hamster')
t= tuple(x)
print(t)

# Adding tuple to a tuple
t = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
t2 = ("hamster",) # without adding comma it will consider as a string
t += t2
print(t)

# Remove items

t = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
x= list(t)
x.remove('apple')
t= tuple(x)
print(t)

# Deleting tuple
t = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
del t
print(t) # Error occurs becaude tuple got deleted


# Unpacking tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

fruits = ('apple', 'banana')
(a,b) = fruits
print(type(a))
print(b)

# Using astrisk # Assigns rest values to the b

fruits = ('apple', 'banana', 'anake')
(a,*b) = fruits
print(a)
print(b) # Assigns rest values to the b

# Using * other than last value

fruits = ('apple', 'banana', 'anake')
(*a,b) = fruits
print(a)
print(b)

# Loop Through a Tuple
fruits = ('apple', 'banana', 'anake')

for x in fruits:
    print(x)

# loop through index value
fruits = ('apple', 'banana', 'anake')

for x in range(len(fruits)):
    print(fruits[x])

# loop using while
fruits = ('apple', 'banana', 'anake')

i = 0
while(i < len(fruits)):
    print(fruits[i])
    i+=1


# Joining tuples using * operator
t1 = (1,2,3)
t2 = (4,5,6)

t3 = t1+t2 # (1, 2, 3, 4, 5, 6)

t4 = t1*2  # (1, 2, 3, 1, 2, 3)

"""
Tuple methods 

count() - returns number of time a specified value occures int he tuple 
index() - returns the index where the element is found 
"""

"""
Tuple sets 
Set
Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed.
Duplicates are not allowed in sets 
"""

# Here false and 0 is considered as same value
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset) # {'banana', False, True, 'cherry', 'apple'}

# To get length of the set

print(len(thisset))

# Setting data types of the sets - We can set any data type, A set can also contain different data type

# thee set constructor

thisset = set(('apple', 1, True))

# accessing the elements of the set

for x in thisset:
    print(x)

# Checking is condition on sets

if 'apple' in thisset:
    print(True)

# adding sets

s1= {'apple', 'banaba'}
s1.add('pine')
print(s1) # {'pine', 'apple', 'banaba'}

# Adding elements from another set to current set
s1= {'apple', 'banaba'}
s2= {'a', 'b'}

s1.update(s2)
print(s1) # {'b', 'banaba', 'apple', 'a'}


# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

s1= {'apple', 'banaba'}
s2= ('a', 'b')

s1.update(s2)
print(s1) # {'a', 'banaba', 'apple', 'b'}

# removing the element from the set

# Using remove method

s1= {'apple', 'banaba'}
s1.remove('apple') # removes apple from the set. If there is no apple shows error
s1.discard('apple') # removes lement but do not show error
s1.pop() # this will remove any random element and returns that element


# Deleting the entire set
s1= {'apple', 'banaba'}
del s1
print(s1) # deleted the set entirly but shows error while printing because there is no set

# looping thorugh the set
# we can only loop through this method because indexing will not work in sets

s1 = {'apple', 'banaba', 1}

for x in s1:
    print(x)

# Joining the sets

s1 = {1,2,3}
s2 = {3,4,5,6}

s3 = s1.union(s2)
s4 = s1 | s2
s1.update(s2) # instead of creating new set it updates the s1

s3 = s1.intersection(s2)
s4 = s1 & s2
s1.intersection_update(s2) # instead of creating new set it updates the s1

s3 = s1.difference(s2)
s4 = s1 - s2
s1.difference_update(s2) # instead of creating new set it updates the s1

s3 = s1.symmetric_difference(s2)
s4 = s1 ^ s2
s1.symmetric_difference_update(s2) # instead of creating new set it updates the s1

