#OOP object oriented programming -a class is a template object implements the class in real world

"""
Advantages of OOP
Provides a clear structure to programs
Makes code easier to maintain, reuse, and debug
Helps keep your code DRY (Don't Repeat Yourself)
Allows you to build reusable applications with less code
Tip: The DRY principle means you should avoid writing the same code more than once. Move repeated code into functions or classes and reuse it.

What are Classes and Objects?
Classes and objects are the two core concepts in object-oriented programming.

A class defines what an object should look like, and an object is created based on that class. For example:"""


class Student:
    #attributes -names,age methods--display
   # -details,displayhook(-email)
   
   def __init__(self,name,course,age):
       self.name = name
       self.course = course
       self.age = age
       
       
    #method to show information
    
   def info(self):
        return f"The student name is {self.name} aged {self.age} and learning {self.course}"
    
    
    
#create an object

mystudent1= Student("Lawrence","MIT",25)
student2 = Student("Grace","Full stack",22)



print(mystudent1.info())
print(student2.info())
       
     