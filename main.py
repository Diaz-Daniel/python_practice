#print("hello world")
#print("This is my first python program")

# Strings
#name = 'daniel'
# print(name)

# checking type
# print(type(name))

#first_name = 'abi'
#last_name = 'diaz'
#full_name = first_name + last_name
#print('Hello' + ' ' + full_name)

# working with numbers
#age = 32
#age += 1
# print(age)
# print(type(age))

# converting int to string when printing result
# this is called a stringcast
#print("this year you will be: " + str(age))

# float datatype (includes numbers with decimal
#height = 250.5
# print(height)
# print(type(height))
#print("an object's height is: " + str(height)+"cm")

# boolean true or false
#human = False
# print(human)
# print(type(human))
#print('are you a human: ' + str(human))

# Multiple Assignment = allows us to assign multiple variables at the same time using one line of code
#name = "daniel"
#age = 21
#working = False
# print(name)
# print(age)
# print(working)

#name, age, working = "daniel", 21, False

#spongebob = patrick = sandy = squidward = 30

# print(spongebob)
# print(patrick)
# print(sandy)
# print(squidward)

# USEFUL METHODS FOR STRINGS
#name = "daniel diaz"
# print(len(name))
# print(name.find("l"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("a"))
#print(name.replace("a", "e"))
# print(name*3)

# TYPE CASTING = convert the data type of a value to another data type
# this is a helpful method because you cannot print a string with an integer using concatonation, so
# converting this is the easiest option
# x = 1  # int
# y = 2.0  # float
# z = "3"  # str

#z = int(z)
# y = int(y)  # this is a long term change to y
# print(x)
# print(int(y)) # this is a short term reassignment to change y from float to int
# print(z)
# print(y)
# print(z*3) # this is possible because on line 74 we changed z to an int
# print("x is an int but is now a short term string " + str(x))


# ACCEPTING USER INPUT
name = input("What is your name?: ")
age = int(input("How old are you?: "))
print("Hello "+name)
