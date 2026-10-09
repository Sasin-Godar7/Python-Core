
# inheritance means that child is accesing its parent property using :

class Animal():
    def prajati(self):
        print("animals are living beings")


class Dog(Animal):
    print("kutte ke bacche ")
    def sound(self):
        print("dog barks")
    print("kukur ho jaat")  

class Cat(Animal):
    print("biralo ko jaat")
    def sound(self):
        print("cat meows")

billi = Cat()
billi.sound()

kutta = Dog()
kutta.sound()
billi.prajati()
        