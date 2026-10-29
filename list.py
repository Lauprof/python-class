#list are data structures that store collections of items. They are ordered, mutable, and allow duplicate elements. Lists can contain elements of different data types, including other lists. In Python, lists are defined using square brackets, and elements are separated by commas.

courses = ["MIT", "Android development", "Java", "C++"]

accessing_elements = courses[0]  # Accessing the first element of the list


print(courses[0])

#mthods to manipulate lists include append(), insert(), remove(), pop(), and sort(). These methods allow you to add, remove, and organize elements within the list.

courses.append("Python")  # Adding an element to the end of the list
print(courses)
courses.insert(2, "Data Science")  # Inserting an element at a specific index
print(courses)
courses.remove("Java")  # Removing an element from the list
print(courses)

courses.pop(2)  # Removing an element at a specific index
print(courses)

courses.sort()  # Sorting the list in ascending order

print(courses)  # Printing the sorted list

print(len(courses))  # Getting the length of the list

for course in courses:  # Iterating through the list using a for loop
    print(course)
    
    


