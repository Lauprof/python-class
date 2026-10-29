#inheritance is a concept in oop that allows a child to inherit methods from  a base class

class Animal:
    #attribute habitat,sound ,name
    def __init__(self,name,age,habitat):
        self.name = name
        self.age = age
        self.habitat = habitat
        
    def __str__(self):
        return f"The animal name is {self.name} and its {self.age} years old and lives in {self.habitat}"
    
    def speak(self):
        return f"the {self.name} makes a sound "
    
        
    
#child class
class Dog(Animal):
    def __init__(self,name,age,habitat,breed):
        Animal.__init__(self,name,age ,habitat)
        self.breed = breed
        
    def speak(self):
        return f"{self.name} barks back" #method overriding
    
    def info(self):
        return f"{self.name} is a  {self.breed}"
        

#CAT CLASS that inherits from animal 


#create a n object

dog1 = Dog("simba",2,"forest","german shepherd")


print(dog1.name)
print(dog1.age)
print(dog1.habitat)
print(dog1.breed)


#calling the speak 

print(dog1.speak())


