#operators in python are special symbols or keywords that perform operations on one or more operands. They can be categorized into several types, including arithmetic operators, comparison operators, logical operators, assignment operators, bitwise operators, and more.


#addition operator (+) is used to add two numbers or concatenate two strings.

x = 5

y = 10

print(f"the sum of two numbers is: {x} + {y} = {x + y}")  # Output: 5 + 10 = 15

#subtraction operator (-) is used to subtract one number from another.
z = 15
w = 5
print(f"the difference of two numbers is: {z} - {w} = {z - w}")  # Output: 15 - 5 = 10


#modulus operator (%) is used to find the remainder of a division operation.
a = 10
b = 3
print(f"the remainder of the division is: {a} % {b} = {a % b}")  # Output: 10 % 3 = 1


#division operator (/) is used to divide one number by another. It returns a float value.

quotient = a / b
print(f"the quotient of the division is: {a} / {b} = {quotient}")  # Output: 10 / 3 = 3.3333333333333335


#exponentiation operator (**) is used to raise a number to the power of another number.
base = 2    
exponent = 3
result = base ** exponent
print(f"the result of the exponentiation is: {base} ** {exponent} = {result}")  # Output: 2 ** 3 = 8


#greater than operator (>) is used to compare two values and returns True if the left value is greater than the right value, otherwise it returns False.
x = 10
y = 5
print(f"is {x} greater than {y}? {x > y}")  # Output: is 10 greater than 5? True

#less than operator (<) is used to compare two values and returns True if the left value is less than the right value, otherwise it returns False.
print(f"is {x} less than {y}? {x < y}")  # Output: is 10 less than 5? False

#equal to operator (==) is used to compare two values and returns True if they are equal, otherwise it returns False.
print(f"is {x} equal to {y}? {x == y}")  # Output: is 10 equal to 5? False


#logical operators in python are used to combine conditional statements. The three logical operators are: and, or, not.

#not operator (not) is used to reverse the logical state of its operand. If the condition is True, it becomes False, and if it is False, it becomes True.

#not operator operates on a single boolean value and returns the opposite boolean value. For example, if the input is True, the output will be False, and vice versa.

print(f"the logical not of {x > y} is: {not (x > y)}")  # Output: the logical not of True is: False



#and operator (and) is used to combine two boolean expressions and returns True only if both expressions are True, otherwise it returns False.


print(f"the logical and of {x > y} and {x < y} is: {(x > y) and (x < y)}")  # Output: the logical and of True and False is: False


#or operator (or) is used to combine two boolean expressions and returns True if at least one of the expressions is True, otherwise it returns False.

print(f"the logical or of {x > y} and {x < y} is: {(x > y) or (x < y)}")  # Output: the logical or of True and False is: True


#!= is the not equal to operator, which is used to compare two values and returns True if they are not equal, otherwise it returns False.

print(f"is {x} not equal to {y}? {x != y}")  # Output: is 10 not equal to 5? True


'''Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator	Description	Example	Try it
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not 


'''

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)


#assignment operators are used to assign values to variables. The most common assignment operator is the equal sign (=), which assigns the value on the right to the variable on the left.

'''
Operator	Example	Same As	Try it
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3
print(x)	
'''
num1 =5

num3 = 10

print(f"the value of num1+=num3 is: {num1 + num3}")


#logical operators are used to combine conditional statements. The three logical operators are: and, or, not.

x = 5

print(not(x > 3 and x < 10))