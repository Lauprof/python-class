# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


#string

greeting="I am in love with my baby"

print(greeting)
print(type(greeting))

# float number is a number, positive or negative, containing one or more decimals. Float can also be scientific numbers with an "e" to indicate the power of 10.

first_number= 5.5
second_number= 10.5

print(first_number)
print(second_number)


#complex number has a real and imaginary part, which is represented as a+bi, where a is the real part and b is the imaginary part.

z = 5 + 3j


print(z)
print(type(z))


#boolean data type is a data type that can only have one of two values, True or False.

medical_state = True

bad_condition = False

print(medical_state)
print(bad_condition)
print(type(medical_state))
print(type(bad_condition))


# Casting in python is therefore done using constructor functions:

# int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals


mynumber ="45"

print(int(mynumber))
print(type(int(mynumber)))


# string to int   
str_number = "45"
print(int(str_number))

print(type(int(str_number)))