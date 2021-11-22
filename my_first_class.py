# creats bluepint of how a object needs to be defined
class Dog:
    animal_kind = "canine" #class variable

    def __init__(self,name,coat_colour):# "dunder init"( double-underscore initialise)
        self.legs = 4
        self.name = name
        self.__colour = coat_colour
        print(self.bark())

    def bark(self):# self reffers to the current class
        return  f"Woof! I am a {self.animal_kind}"
    def get_colour(self):
        return self.__colour
    def set_colour(self, new_colour):
        self.__colour = new_colour


fido = Dog("Fido","black") #instantiation(insance)
print(fido, type(fido))
lassie = Dog("Lassy","brown & white")
print(fido.bark())
print(fido.legs)
print(lassie.legs)

Dog.legs = 8

print(fido.legs)
fido.legs = 6
print(fido.legs)
fido.__colour = 3.14
fido.legs = 324
print(fido.__colour, fido.legs)
print(fido.get_colour())
print(fido.set_colour("green"))
print(fido.get_colour())
fido.__colour = "red"# sets up a new thingy but does not change the attribute
print(fido.get_colour())
print(fido.__colour)
fido.soon = "cool"
print(fido.soon)
fido.tail = True


