#dictionaries are data structures that store collections of key-value pairs. They are unordered, mutable, and do not allow duplicate keys. Dictionaries can contain elements of different data types, including other dictionaries. In Python, dictionaries are defined using curly braces `{}`, with keys and values separated by colons `:` and pairs separated by commas.

student = {
    "name": "John Doe",
    "age": 21,
    "major": "Computer Science",
    "courses": ["MIT", "Android development", "Java", "C++"]
}

print(student["name"])  # Accessing the value associated with the key "name"
print(student["age"])   # Accessing the value associated with the key "age"
print(student["major"]) # Accessing the value associated with the key "major"
print(student["courses"]) # Accessing the value associated with the key "courses"   

student["age"] = 22  # Updating the value associated with the key "age"
print(student["age"])  # Printing the updated value of "age"

student["graduation_year"] = 2024  # Adding a new key-value pair to the dictionary
print(student)  # Printing the updated dictionary

#methods to manipulate dictionaries include `get()`, `keys()`, `values()`, `items()`, and `pop()`. These methods allow you to retrieve values, get keys, get values, get key-value pairs, and remove items from the dictionary.


print(student.get("name"))  # Using the get() method to retrieve the value associated with the key "name"
print(student.keys())  # Using the keys() method to get all the keys in the dictionary  
print(student.values())  # Using the values() method to get all the values in the dictionary
print(student.items())  # Using the items() method to get all the key-value pairs in the dictionary

for key, value in student.items():  # Iterating through the dictionary using a for loop
    print(f"{key}: {value}")  # Printing each key-value pair in the dictionary