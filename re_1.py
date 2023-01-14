# class Person:
#     counter = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Person.counter += 1
    
#     def greet(self):
#         return f"Hi, It's {self.name}."

#     @classmethod
#     def createAnonymous(cls):
#         return Person('Anonymous', 22)
    
#     @staticmethod
#     def celsius_to_farenheit(c):
#         return 9 * c / 5 + 32

#     @staticmethod
#     def farenheit_to_celcius(f):
#         return 5 * (f-32) / 9

# class Employee(Person):
#     def __init__(self, name, age, job_title):
#         super().__init__(name, age)
#         self.job_title = job_title
    
#     def greet(self):
#         return super().greet() + f" I am a {self.job_title}."

# p1 = Person('Farhad', 28)
# e1 = Employee('Farhad', 27, 'Python developer')

# print(p1.greet())
# print(e1.greet())

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

l1.reverse()
l2.reverse()

l1_number_str = ''
l2_number_str = ''

l1_number = int(l1_number_str.join(str(x) for x in l1))
l2_number = int(l1_number_str.join(str(x) for x in l2))

addition_result = l1_number + l2_number

res = [int(x) for x in str(addition_result)]
res.reverse()

print(res)



 

