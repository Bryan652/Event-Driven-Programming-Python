"""
For better understanding of the codes with explanation heres the link 
https://www.w3schools.com/python/default.asp
"""

# Python Syntax
print("Hello World\n")

# indentation 
print("Indentation")
if 5 > 2:
    print("True\n")
elif 5 == 2: 
    print("5 is equal to 2")
else: 
    print("False")

# Variables 
a = 5
A = 1

x, y, z = "Apple", "Banana", "Cherry"
print("Variables")
print(x, y, z)
print(x, "Hmmm?", z)
print(x + y + z,"\n\n")

# Global variables
print("Global variables")
v = 1

def myFunc(): 
    global v
    v = "fantastic" # if this isn't global the display will be 1
    print("this is", v)

myFunc()
print("this is", v, "\n\n")

"""
Data Types 

Text Type: 	    str

Numeric Types: 	int, float, complex

Sequence Types: list, tuple, range

Mapping Type: 	dict

Set Types: 	    set, frozenset

Boolean Type: 	bool

Binary Types: 	bytes, bytearray, memoryview

None Type: 	    NoneType
"""

# Python numbers 
x = 1 # int 
y = 2.6 # float 
z = 1j # complex

print("Python numbers")
print(type(x))
print(type(y))
print(type(z), "\n\n")

# Python Casting
#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print("Python casting")
print(a)
print(b)
print(c, "\n\n")

# other casting 
print("Python string casting")
x = str(2)
y = str(2.6)
z = str("HEllo")
print(x, y ,z, "\n\n")

print("Python modification")
x = str("Hello World")
print(x.upper())
print(x[2:5])
print(x[2:])
print(x[:5])
print(x[-5:-2])

y = "       Hello, World!"
print(y.strip()) # Remove whitespace
# you can assign this to a variable if needed y = y.strip()
print(y.replace("Hello", "Hi"))
print(y.split()) # this will result to ['Hello,', 'World!'] you can also assign this to a variable
a = "Hello"
b = "World"
print(a, b) # Concatenation

# Format string 
name = "Bryan"
age = 30 
greet = f"My name is {name} and i am {age} years old." # You can also change the format of the value {age:2f}
print(greet, "\n\n")

# Escape characters 
# https://www.w3schools.com/python/python_strings_escape.asp
# Ex: 
txt = "We are the so-called \"Vikings\" from the north."
print(txt, "\n\n")

# String methods 
# https://www.w3schools.com/python/python_strings_methods.asp

# Python Booleans 
print(2 > 1)
print(2 < 1)
print(2 == 1)
print(2 != 1)
print(2 >= 1)
print(2 <= 1, "\n")
x = True
y = False 

if 5 > 2: 
    x = False 
    print(x)

# For more information on python booleans https://www.w3schools.com/python/python_booleans.asp

def myFunc(): 
    return True 

if myFunc(): 
    print("myFunc return", True, "\n\n")
else:
    print("myFunc return", False)

# Operators 
# For more information about python operators https://www.w3schools.com/python/python_operators.asp
# is/ is not
# in/ not in
# and/or/not

# python list 
print("Python List")
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(thislist[0])
print(thislist[1])
thislist[0] = "Kiwi"
thislist[1:3] = ["watermelon", "Dragon Fruit"]
thislist.append("orange") # this will always go to the end
thislist.insert(1, "orange") # this will be inserted at a specific index
print(thislist, "\n\n")

# Extend
print("Extend")
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist, "\n\n")

# Remove 
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print("REMOVE", thislist, "\n\n")

# Pop
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print("POP", thislist, "\n\n")

# del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print("DEL", thislist, "\n\n")

del thislist # remove the entire list

# Loop through the list 
print("\n\nLOOP")
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
for x in thislist:
    print(x)

# For index of the list 
print("Index")
for i in range(len(thislist)): 
    print(thislist[i])
    print(i)

# while loop
print("\n\nusing while loop")
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

# Shorthand Loop
print("\n\nusing shorthand loop")
[print(x) for x in thislist] 

# List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

# Items that have "a" will be added to the new list
for x in fruits:
  if "a" in x: 
    newlist.append(x)

print(newlist, "\n\n") 

# Shorthand
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist, "\n\n")

# For more information about that https://www.w3schools.com/python/python_lists_comprehension.asp

# sorting 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # sort alphabetically 

# Copying a list 
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Joining a list 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 

# List methods https://www.w3schools.com/python/python_lists_methods.asp

# Just look into the w3Schools everything is in there and if you wanna try stuff do it in the test file 
# If the code is slow use hashmap