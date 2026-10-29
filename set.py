#sets are unordered collections of unique elements in Python. They are defined using curly braces {} or the set() constructor. Sets support various operations such as union, intersection, difference, and symmetric difference. They are useful for removing duplicates from a collection and for performing membership tests efficiently.

fruits = {"apple", "banana", "cherry", "date"}

print(fruits)  # Printing the set of fruits

print(len(fruits))  # Getting the length of the set


for fruit in fruits:  # Iterating through the set using a for loop
    print(fruit)