#tuples are immutable sequences in Python, meaning that once a tuple is created, its elements cannot be changed, added, or removed. Tuples are defined by enclosing elements in parentheses `()`, and they can contain elements of different data types, including other tuples. They are often used to group related data together and can be used as keys in dictionaries due to their immutability.


courses = ("MIT", "Android development", "Java", "C++")

print(courses[0])  # Accessing the first element of the tuple  

print(len(courses))  # Getting the length of the tuple
print(type(courses))  # Getting the data type of the tuple

for field in courses:  # Iterating through the tuple using a for loop
    print(field)