class Fruit:
    # This is a constructor
    def __init__(self, name, size, colour, price, seed_color="none"):
        self.name = name
        self.size = size
        self.colour = colour
        self.price = price
        self.seed_color = seed_color
class Car:
    def __init__(self, model, color, horse_power, price):
        self.model = model
        self.color = color
        self.horde_power = horse_power
        self.price = price
class Employee:
    def __init__(self, name, gender, ID_number, department, salary):
        self.name = name
        self.gender = gender
        self.ID_number = ID_number
        self.department = department
        self.salary = salary
class Student:
     def __init__(self, name, email, password):
         self.name = name
         self.email = email
         self.password = password

     def register(self):
        print("You register with email", self.email,
              "and password", self.password)

     def login(self):
        # Assume the user had already registered
       if self.email == "abc@gmail.com" and self.password == "123":
         print("login successful")
       else:
        print("wrong user name or password")

class Teacher(Student):
    def __init__(self, name, email, password, gender, salary):
        self.name = name
        self.email = email
        self.password = password
        self.gender = gender
        self.salary = salary

    def suspend_student(self):
        print("Yeah i can suspend a student")

class Principal(Teacher):
    def suspend_teacher(self):
        print("Yeah i can suspend a teacher")

# Write a python logic to implement a simple calculating
# Capable of computing any two numbers entered by the user in the input
# Make sure the logic can perform all the four mathematical operation