"""
A programming language is object oriented programming language when it follows the object oriented principle.
1) Inheritence
2) polymorphism
3) Encapsulation

Inheritency: it is the way object or class uses or inherits attributes and functions from other object or class.
it is used to reuse the code.

2) encapsulation: it is data hiding principle. In this, it doesnt matters how attributes or functionality are implemented rather than to
know how to use them.

3) Polymorphism: Polymorphism means many forms. In programming, it means same functionality name can be used with different objects or classes.

Class: Class is blueprint or main functions from which are objects are created. it has attributes and methods.

Object: it is an instance of a class.
"""


class dress:
    x = 5


p1 = dress()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_function(self):
        print("My name is ", self.name)


p2 = Person("Rohit", 32)

p2.my_function()

print(p2.name, p2.age)


class Rohit:
    def __init__(self, company, rounds):
        self.company = company
        self.rounds = rounds

    def interview(self):
        print("Rohit has appeared for interview with company name = ", self.company)
        print("his interview round was ", self.rounds)




p3 = Rohit("Rohit", 3)
p3.interview()
