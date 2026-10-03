
 # hiding the sensetive or implementation details of a class and only showing the essential features to the user is absreaction 


# abstraction 

# class Car:

#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def startCar(self):
#         self.clutch = True
#         self.acc = True
#         print("now car is start and moving")

#     def stopCar(self):
#         self.clutch = True
#         self.brk = True
#         print("now the car is stopped")    


# lambo = Car()
# lambo.startCar()
# lambo.stopCar()






from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
        print("dog is not dangerous")
        def sound(self):
            print("dog barkss ...")


class Cat(Animal):
        print("cat is cute creature")
        def sound(self):
            print("cats meowsss ....")


d = Dog()
d.sound()

c = Cat()
c.sound()