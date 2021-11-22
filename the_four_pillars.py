# # there are four pillars(strength) of object oriented programming languages
#
# # Abstraction
#     # making life easier for the user by providing obvious inputs / outputs
#
#
# # Encapsulation
#     # private variable
#
# # Inheritance
#     #passing on attributes and methods to avoid repetition
#
# # Polymorphism
#     # many forms
# class Animal:
#     def __init__(self, legs):
#         self.alive = True
#         self.legs = legs
#
#     def breathe(self):
#         print("breate in ..... breate out")
#     def eat(self):
#         print("npom nom nom")
#     def reproduce(self):
#         print("giving birth")
#
# class Mammal(Animal):
#     def __init__(self,legs):
#         super().__init__(legs)# run the initization for above class
#         self.warm_blooded = True
#
# class Cat(Mammal):
#     def __init__(self,legs):
#         super().__init__(legs)
#     def reproduce(self):
#         print("over ride")
#
#
# # cat = Mammal()
# # print(cat.warm_blooded)
# # cat.breathe()
# # print(cat.alive) # no two method with same name
# horse = Mammal(4)
# cat = Cat("shorthair")


# create a rectangle class
#lenght nd width attributes
#perimeter metod to retun perimeter
#area metod
#create square class
# side_length attribute
#perimeter and area metod

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def perimeter(self):
        return 2 * (self.length + self.width)
    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self,side_length):
        self.side_length = side_length
        self.length = side_length
        self.width = side_length


sq = Square(3)
print(sq.area())
print(sq.perimeter())


