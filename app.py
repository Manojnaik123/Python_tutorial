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

'''
Python dictionaries
'''

# Creating and printing dictionaries
# dictionaries are changable that means we can add or remove key value pairs

t = {
    'name' : 'manoj',
    'age' : 24
}

print(t)
print(t['name']) # This way we can refer values using the key

# Duplicates are not allowed in the dict
# Duplicate values will overwrite the existing value

t = {
    'name' : 'manoj',
    'name' : 'naik'
}

print(t)
"""
/ this will print {'name': 'naik'}
"""

# Dict length can be known using the len function

print(len(t))

# Dict - The valus can be of any datatype

t ={
    'name' : 'manoj',
    'age' : 24
}

# Dict constructor
thisdict = dict(name = 'manoj', age = 24)
print(thisdict)

# Accessing the items in dict

t = {
    'brand' : 'ford',
    'model' : 'mustang'
}

x = t['brand']

# There is also a method called get() which does same as the above

x= t.get('model')

# There is also a method called as keys that will return all the keys of the dict

x = t.keys() # the list of the keys this return is the view of the dict any changes int eh dict will reflect in this list

# The items() function will return all teh elements of the dict as the tuple

x = t.items()
print(x) # prints dict_items([('brand', 'ford'), ('model', 'mustang')])

# Check is keys exist

if 'name' in t:
    print(True)

# Change the items of the dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018 # Changes the year to 2018

thisdict.update({"year": 2018}) # Changes the year to 2018

# Adding items to the dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict['color'] = 'red'

# Using update also we can do the same

thisdict.update({'color': 'red'})

# Remove items

thisdict.pop('color')
thisdict.popitem() # this removes the last inserted key value pair
del thisdict['color'] # this removes the single key value pair
del thisdict # deleted the entire dict

thisdict.clear() # empties the dict

for x in thisdict:
    print(x) # This prints the key one by one

for x in thisdict:
    print(thisdict[x]) # This prints the key one by one

# we can also print vales using values() amnd for loop

for x in thisdict.values():
    print(x)

# similar to the keys
for x in thisdict.keys():
    print(x)

# loop through both key and value using the items()
for x,y in thislist.items():
    print(x,y)

# Copy a dict
# Make a copy using the copy()

t = {
    'name' : 'manoj',
    'age' : 24
}

b = t.copy()
print(b)

# Make a copy using the dict()
t = {
    'name' : 'manoj',
    'age' : 24
}

b = t.dict()
print(b)

# nested dictionaries
# A dict can have dict in itself called nested dict

myfamily = {
    'member1' : {
        'name' : 'manoj',
        'age' : 25
    },
    'member2' : {
        'name' : 'prema',
        'age' : 50
    }
}

# using three dict to create new dict
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# Accessing items from the nested dict

print(myfamily['child1']['name'])

# Looping through the nested dict

for x, obj in myfamily.items():
    print(x)
    for a in obj:
        print(a+ ':' , obj[a])

# If else statement
'''
Python supports the usual logical conditions from mathematics:
    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b
'''

# Syntax
a = 33
b = 200
if b> a:
    print("b is greater than a")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")

# there is also the nested if statement that i know

# Short hand if
if a>b: print("a is greater than b")

# Short hand if else
print("A") if a> b else print('B')

# similarly we can use and or and not in the if statement

if(a>b & a== b):
    print("True")

# pass Keyword - it is used to pass the if statement if we do not intend to do anything

if a>b:
    pass # if we leave this without anything this will show error


# Python match - The match statement is used to perform different actions based on different conditions.
# This is similar to the swithch

# Syntax
day = 4
match day:
    case 1:
        print('1')
    case 2:
        print('2')
    case 3 | 4 |5:
        print('3,4,5')
    case _:
        print('no match') # this is the default cace

# there is also 'If Statements as Guards'
# do think is much important

# While loops
i = 0
while i < 5:
    print(i)
    i+=1

# The break statement
# Exit the loop when i is 3:

i = 1
while i< 6:
    print(i)
    if i == 3:
        break
    i+=1

# the continue statement
#With this we can stop the current iteration

i=0
while i < 6:
    i += 1
    if(i == 2):
        continue
    print(i)

# the else statement

i=0

while i < 6:
    print(i)
    i += 1
else:
    print('i is no longer than 6')

# For loops
# The for loop cannot be empty instead we can use pass
for x in [0, 1, 2]:
  pass

# Looping through strings

for x in 'bannana':
    print(x)

# Using the break statement

for x in 'bannana':
    print(x)
    if x == 'a':
        break

# This prints 'ba'

# The continue statement
for x in 'bannana':
    if x == 'n':
        continue
    print(x)

# The range function
for x in range(6):
    print(x)

for x in range(2,6): # range start from 2 to 6, but does not include 6
    print(x)

for x in range(3, 15, 2): # starts with 3 to 15 doesnot include 15 and the third paramenter is increment value
    print(x)

# prints 3 5 7 9 11 13

# Else in for loop

for x in range(5):
    print(x)
else:
    print(' Range over ')

# In case of continue the else part will run
for x in range(5):
    if x == 3:
        continue
    print(x)
else:
    print(' Range over ')

# In case of break the else part wont run
for x in range(5):
    if x == 3:
        break
    print(x)
else:
    print(' Range over ')


# Nested for loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)

# Python functions
# To create a function in the python we use def keyword
# Syntax
def function_name():
    print('hello world')


# Functions with arguments

def function_one(name): # Similarly we can set multiple arguments
    print(name + " helo ")

# Using arbitary arguments , *args

def function_one(age, *name):
    print(name[0])
    print(name[1])
    print(age)

function_one(24, 'manoj', 'naik')

# Keyword argument

def function_one(age, name):
    print(name)
    print(age)

function_one( name = 'manoj', age = 24)

# aribitary keywords **kwargs

def function1(**arr):
    print(arr['name'])
    print(arr['age'])

function1(age = 21, name = 'manoj naik')

# default parameter value

def addition(a = 1, b=1):
    print(a + b)

addition() # there are no parameters so the function takes the default value

# passing a list as an argument in pythons function

a = [1,2,3,4,5]
def func(b):
    for x in b:
        print(x)
func(a)

# Returning values in function

def func(x):
    return x

i = func(1)

print(i)

# pass keyword - Function definitions cannot be empty,
# but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.

def myfunction():
  pass

# Positional-Only Arguments - Function with arguments can also accept keyword and positional arguments.
# To disable this action we can use / in the argument as the below example.

def func(x, /):
    print(x)

func(3) # this will print 3
func(x = 3) # this will throw error

# Keyword only arguments - Function with arguments can also accept keyword and positional arguments.

def func(*, x):
    print(x)

func(3) # this will throw error
func(x= 3) # this will not throw error

# Combining positional and keyword only arguments

def func(a,b,/,*, c,d):
    print(a,b,c,d)
func(1,2,c=3, d=4)

# Recursion

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

# Lambda - is a small and anonyms function

x = lambda x: x+10
print(x(5))


# Multiple arguments

x= lambda a,b: a+b
print(x(1,2))

# here is one of the reason to use the lambda function

def func(a):
    return lambda x: x*a

number_doubler = func(2)
print(number_doubler(10)) # Here 10 is doubled

number_tripler = func(3)
print(number_tripler(10)) # Here 10 is tripled

# Python array
# This Shows how to use list as array in python

# Creatign an array
arr = ['volvo', 'benz', 'honda']

# Accessing element from the array
print(arr[0]) # print first element

# Modifying the element in the array
arr[1] = 'mercedes'

# Prints the length of the array
print(len(arr))

# adding element in the array
arr.append('toyota')

# removing the element from teh array
arr.pop()  # removes the last element

arr.pop(0) # removes element from the index

arr.remove('honda')

# Looping through the array is same as the list using for loop and for loop using range

# OOPS
class NewClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} : {self.age}'

    def func(self, a,b):
        return f"{self.name}'s age is grater than {a+b}"



obj1 = NewClass('manoj', 24)


# Modifying objects properties
obj1.name = 'kunjal'

# Deleting the object's property
del obj1.name

print(obj1.func(1, 2))

# The pass statement
# Class definition cannot be empty so we can use pass instead
class Person:
  pass

# Inheritance
'''
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
'''

# Creating a parent class - Any class can be a parent class, so the
# syntax to create the parent class is same as the normal class

# Creating the child class

class Human:
    def __init__(this, name, age):
        this.name = name
        this.age = age

    def print_details(this):
        return f'{this.name}\n {this.age}'

class Student(Human):
    def __init__(this, name, age, roll_no):
        Human.__init__(this, name, age)
        this.roll_no = roll_no

    def __str__(this):
        return f'{this.name},{this.age},{this.roll_no}'

obj = Student('John', 22, 32)

print(obj)

class Human:
    def __init__(this, name, age):
        this.name = name
        this.age = age

    def print_details(this):
        return f'{this.name}\n {this.age}'

class Student(Human):   # For inheritance in child class refer the parent
    def __init__(this, name, age, roll_no): # in this func add the new property
        Human.__init__(this, name, age) # and refer parent __init__ function, We cal also call Super().__init__(this, name, age)
        this.roll_no = roll_no # then assign the property

    def __str__(this):
        return f'{this.name},{this.age},{this.roll_no}'

obj = Student('John', 22, 32)

print(obj)

# Iteration - Got through the meaning - more clarity needed

#Polymorphism
# The word "polymorphism" means "many forms",
# and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

# len() is an example of the polymorphism because it can be used on lit,  tuple, string, and dict

# This is another example of polymorphism
class Car:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print('run')


class Boat:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print('sail')


class AirCraft:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print('fly')

car = Car('toyota')
boat = Boat('lamb')
aircraft = AirCraft('gulf')

for x in (car, boat, aircraft):
    x.move()


# Inheritance class polymorphism
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print('run')

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print('sail')


car = Car('bmw')
boat = Boat('lamb')

for x in (car, boat):
    x.move()

# Pyhton scope
# Local scope - A variable created inside the function is availabe inside the function
# Function inside function

def func1():
    x = 5
    def func2():
        print(x)
    func2()

func1()


# This will print global x
x = 10
def func1():
    x = 5
    def func2():
        global x
        print(x)
    func2()

func1()

# This will print previous function x
x = 10
def func1():
    x = 5
    def func2():
        print(x) # prints 5
    func2()

func1()

# nonlocal - its usage will refer to the variabel of the outer function

# Example
def func1():
    x = 5
    def func2():
        x = 33  # this creates a new variable and dosent refers to the outer func variable
        print(x) # prints 33
    func2()
    print(x) # prints 5
func1()

def func1():
    x = 5
    def func2():
        nonlocal x
        x = 33
        print(x) # prints 33
    func2()
    print(x) # prints 33
func1()

# What is a module?
# A module can be considered same as a code library
# Naming a module - we can name anything we want but it should end with .py

# This is how we import from module
# mymodule.py
def greeting():
    print('Hello')

object1 = {
    'name': 'John',
}

# mail.py
import mymodule

mymodule.greeting() # importing function

print(mymodule.object1['name']) # importing variables

# using the dir() - it will list all the methods and variables in the imported module
import mymodule

print(dir(mymodule))

# renaming the module
import mymodule as x

print(x.object1)

# We can choose import only part using the from keyword
#mymodule.py
def function_add():
    print('hello')

obj1 = {
    'name' : 'manoj',
    'age' : 22,
}

#newmodule.py
from mymodule import function_add  # This will only import function_add

print(function_add())

# Datetime
import datetime
x = datetime.datetime.now()

print(x.year)
print(x.time())
print(x.date())
print(x.day)

# Python math
x= min(3,2,1)
y= max(3,2,1)

print(x)
print(y)

z= abs(-7.25)

print(pow(2,3)) # this will return the value of x to the power y

# The math module
import math

print(math.sqrt(3))
print(math.ceil(2.4))
print(math.floor(2.4))
print(math.pi)

# Python json
import json

# Converting json into python
x= '{"name":"manoj"}'

y = json.loads(x)

z= json.dumps(y)

print(type(y)) # prints dict
print(type(z)) # prints string

# Regular expression
import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search('rain', txt)
print(x.start()) # 4
print(x.end())# 8

o = re.sub('h', 'x', txt)
print(o) # Txe rain in Spain

t = re.split('\s', txt)
print(t) # ['The', 'rain', 'in', 'Spain']

print(x.span()) # (4, 8) the tuple of the start and end point if the serching text
print(x.string) # returns the passed string into the function
print(x.group()) # Prints the part of the string where there is a match

print(re.findall('a', txt)) # returns the list of all the matches ['a', 'a']

#PIP
# First install the package using pip install camelcase

import camelcase

c= camelcase.CamelCase()

txt ="hello world"

print(c.hump(txt))

# remove package
# pip uninstall camelcase

# Listing all installed packages - pip list

# Try Except
'''
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''

try:
    print(x)
except:
    print('error occured')
else:
    print('no error')
finally:
    print('this runs anyways')

# Multiple excemptions
try:
    print(x)
except NameError:
    print('error occured')
except:
    print('error occured')
finally:
    print('this runs anyways')

# raising an exception
x = -1
if x < 0:
    raise Exception('no numbers below zero')

# String formating

s = 'This is a string' # normal string

f = f'{'manoj'} is a genious. He is {21} years old'

print(f)

# String format

price = 49
tat = 'the price of the product is {}'
print(tat.format(price))

# operations in the string format
a = b =2
d= f' the addition of a and b is {a+b}'

print(d)

# if else in the string format
r = f' {"manoj" if True else "kunjal"}'

print(r)

# executing function ins the string format
y = f'{"RangeRover".upper()}'

print(y)

# multiple values

x = 'manoj'
y = 'naik'

rt = 'firstname: {}, lastname:{}'
print(rt.format(x,y))

# index number
# You can use index numbers
# (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:

x1 = 'manoj'
y1 = 'naik'

rt = 'firstname: {1}, lastname:{0}'
print(rt.format(y1,x1)) # prints - firstname: manoj, lastname:naik

# Named index
xa = 'manoj'
yb = 'naik'

rt = 'firstname: {a}, lastname:{b}'
print(rt.format(a= xa, b = yb)) # prints - firstname: manoj, lastname:naik

# Printing decimal

pr = 45
tt = f'the price is {pr:.2f}'
print(tt) # - the price is 45.00

rate = 500000
print(f'price is {rate:,}') # - price is 500,000

# Python user input
print('enter name')
name = input()

# using prompt with in the input
name = input('enter name')

# getting numerical input
num = int(input('enter num'))

print(type(num))

# validating a number
x = True

while x:
    y = input('enter a number')
    try:
        d = int(y)
        x = False
    except:
        print('wrong input')

print('we got the number')

#____________________________________________________________________________
#____________________________________________________________________________
#____________________________________________________________________________

# File handling
'''
File handling
the key function in this is open() - This function takes two parameter that is filename and mode
There are four diff modes for opening a file they are

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition we can also specify
't' - text - default value - text mode
'b' - binary - binary mode (eg images)
'''

# to open a file
f = open('demo.txt', 'rt') # r means read and t means text

# Python file open

f1 = open('demo.txt') # by default read and default text
# if file located in other location we can specify the location

# r = open(r'C:\Users\Admin\Downloads\rat.txt') # this way

# Using with statement
with open('demo.txt') as x: # by default read
    print(x.read())

# read only parts of the file
with open('demo.txt') as x: # by default read
    print(x.read(2)) # prints first 2 charecters

# Reading one line of the file using readline()
with open('demo.txt') as x: # by default read
    print(x.readline())

# Reading two line of the file using readline()
with open('demo.txt') as x:  # by default read
    print(x.readline())
    print(x.readline())

# looping through the lines
with open('demo.txt') as f:
    for x in f:
        print(x)

# python write and create
# creating a new file

d = open('new_file.txt', 'x')


# writing on the existing file
with open('demo.txt', 'a') as rt:  # 'a' appends the file
    rt.write('this is the last line')
    print(rt.read())

# Overriding the existing file
with open('demo.txt', 'w') as rt:  # 'w' overrides the file
    rt.write('this is the last line')
    print(rt.read())

# deleting the files
import os
os.remove('file_to_be_removed.txt')

# checking if file exist

if os.path.exists('file_to_be_removed.txt'):
    os.remove('file_to_be_removed.txt')
else:
    print('file does not exist')

# deleting the folder
os.rmdir('folder_to_be_removed')

# Duck typing
# Duck typing is a concept in Python (and other dynamically typed languages)
# where the type or class of an object is less important than the methods or behavior it supports.

class Duck:
    def sound(self):
        print("Quack!")

class Dog:
    def sound(self):
        print("Woof!")

def make_sound(animal):
    animal.sound()

# Both work, even though one is Duck and other is Dog
make_sound(Duck())  # Quack!
make_sound(Dog())   # Woof!

# Here, make_sound() function doesn’t care if the object is a Duck or Dog.
# As long as the object has a .sound() method, it works fine.

# Multi dimentional array
a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(a[0])
print(a[0][1])

for x in a:
    for y in x:
        print(y, end='')
    print()

# Decorators
# It modifies the behavious of a function without chaging its actual code

def dec_func(fun):
    def wrapper():
        print('before')
        fun()
        print('after')
    return wrapper

@dec_func
def func():
    print('hello')

func()

# Operator overloading
# Intiger and string knnows what to do with the +, but the object doest know what to do with it.
# When we specify what object should do with the + that is called operator overloading

a = 1
b = 2
print(a+b) # prints 3
print(int.__add__(a,b)) # prints 3, __add__ is the function that int class will call for the addition

# In case of the object, it dosent know what to perform witn +
# Here we will spcify what the + does in object

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other): # it takes two parameters
        ma = self.m1 + other.m1
        mb = self.m2 + other.m2
        return Student(ma, mb)

    def __gt__(self, other):
        ma = self.m1 + self.m2
        mb = other.m1 + other.m2
        if(ma > mb):
            return Student(self.m1, self.m2)
        else:
            return Student(other.m1, other.m2)

s1 = Student(21, 23)
s2 = Student(11, 13)

s3 = s1 + s2
s4 = s1 > s2

print(s3.m1, s3.m2)

# Method overloading - Means multiple methods with same name but different paramenters
# #Python dosent this featurer directly - so we need to impliment accordingly
class Example:
    def show(self, x=None, y=None):
        if x is not None and y is not None:
            print("Two arguments:", x, y)
        elif x is not None:
            print("One argument:", x)
        else:
            print("No arguments")

obj = Example()
obj.show()
obj.show(10)
obj.show(10, 20)

# Python dosent has pointer like c++ or c

# Abstract class - it is a blueprint class that other sub class needs to implement
# All the abstract methods within the abstract class should be in the sub class

# Exampele
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def legs(self):
        pass

class Dog(Animal):
    def sound(self):
        print('woof woof')

    def legs(self):
        print(4)

d = Dog()
d.sound()

# Abstract method - it is the method in the base class that is declared but not defined
# in python we use @abstractmethod to define them, as we saw in the above example

#iterators
# it has a special function iter and next using this they access elements one by one
a = [1,2,3]

b = iter(a)

print(next(b))
print(next(b))
print(next(b))

# Generators
# These are special type that produces values on the fly
def gen():
    yield 5
    yield 1
    yield 1
    yield 1

values = gen()
print(next(values))
print(next(values))
print(next(values))

# generator loop
def gen_fun(n):
    for x in range(1, n+1):
        yield x

a = gen_fun(10)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
