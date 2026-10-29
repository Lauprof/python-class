#a string is a sequence of characters


first_name = "Lawrence"
last_name = 'prof'

#concatenation

fullname = first_name + " " + last_name

print(fullname)


text = "python"


print(text[0])
print(text[-1])

#slicing (start,stop(excluded))


print(text[0:3])
print(text[2:])
# The [::2] syntax uses Python's string slicing template: [start:stop:step].
# • start and stop are empty: This tells Python to scan the entire string from beginning to end.
# • step is 2: This tells Python to skip every second character.

print(text[::2])

#string methods upper,lower

print(text.upper())

greet ="good morning"

print(greet.title())

print(greet.replace('morning',"evening"))

#string formatting

print(f"my name is {first_name } {last_name}")


#escape characters \n \t \'

print("this is \n python")
print("name \t age")
print("\"python is easy \" - mary jane ")

print("he said \" I love python\"")


course = "fullstack"

print(course[0:4])

print(course[4:])
print(course[1:5])
print(course[0:7])