# class Circle():

#     pi = 3.14

#     def __init__(self, radius=1):
#          self.radius = radius
    
#     def area(self):
#         return self.radius * self.radius * self.pi

#     def circ(self):
#         return 2 * self.pi * self.radius

# my_circle = Circle(radius=10)
# print(my_circle.radius)
# print(my_circle.area())
# print(my_circle.circ())

class Animal():

    def __init__(self, fur):
        self.fur = fur
    
    def report(self):
        print('Animal')
    
    def eat(self):
        print('Eating')


class Dog(Animal):
    
    def __init__(self, fur):
        Animal.__init__(self, fur)
        print('Dog created')
    
    def report(self):
        print('I am a dog')

# a = Animal()
# a.eat()
# a.report()

d = Dog('Short')
d.eat()
d.report()
print(d.fur)