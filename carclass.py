class Car:
    def __init__(self, model, origin, maxspeed):
        self.model = model
        self.origin = origin
        self.maxspeed = maxspeed

    def getInfo(self):
        return f"The car model is {self.model} from {self.origin} at top speed {self.maxspeed} km/h."

    


car1 = Car("Toyota Corolla", "Japan", 180)
car2 = Car("BMW M3", "Germany", 250)
car3 = Car("Huawei AITO M9", "China", 220)
car4 = Car("Xiaomi SU 9", "China", 250)

print(car1.getInfo())
print(car2.getInfo())
print(car3.getInfo())
print(car4.getInfo())
