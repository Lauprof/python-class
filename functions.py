#function is a reusable block of code that performs a certain function


#only learn when it is called


def greet():
    print("Greetings good evening")

#calling the function


greet()

#parameters are passed when calling the function

def greetName(name):
    print(f"Greetings {name} welcome")


greetName("Lawrence")


def display_name(name,age):
    print(f"Hello {name} congrats you are {age}  years old")



display_name("Grace",22)

def display_details(name,age, course="MIT"):
    print(f"My name is {name} aged {age} and I am studying {course}")


display_details("prof",25,"Data science")

# area of rectangle
# area of circle
# check if even or odd
# return keyword
#multiplies 3 numbers 
#lamba anonymous 



def addTwoNumber(num1,num2):
    sum = num1 + num2 
    #print(f"The sum of {num1} and {num2} is {sum}")
    return sum


print(addTwoNumber(67,56))

result = addTwoNumber(70,3535)

print(f" The sum is {result}")



    
