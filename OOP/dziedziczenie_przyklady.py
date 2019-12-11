class Animal:
    def __init__(self, name):
        self.name = name
        self.energy = 100

    @property
    def is_alive(self):
        return self.energy > 0

    def move(self, distance):
        self.energy -= 0.1 * distance
        if self.is_alive:
            return distance
        return self.is_alive


    def eat(self, calories):
        self.energy += 0.2 * calories

class Dog(Animal): # dziedziczenie

    def __init__(self, name, species):
        super().__init__(name)# bierze to co na gorze
        #super(Dog, self).__init__(name) to samo
        #Animal.__init__(self,name)
        self.species = species

    def bark(self):
        print("How how")
        self.energy -=0.01


pass

a = Animal("Zenek")
azor = Dog("Azor","Owczarek")
print(a.move(50))
print(a.move(5000))
print(azor.bark())
#print(a.bark)

