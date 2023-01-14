'''
An object is container which contains state and behavior
A class is a blue print for creating objects
In python, a class is alson an object, which is an instance of type

Source : https://www.pythontutorial.net/python-oop/python-class/

'''

class Person:
    pass

person = Person()
print(hex(id(person)))

print( isinstance(person, Person), Person.__name__, type(Person), isinstance(Person, type) )