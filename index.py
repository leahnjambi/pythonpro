from main import Fruit, Car, Employee, Student, Teacher, Principal
# Start creating fruits out of the Fruit class
fruit_one = Fruit("Mango", "200g", "Green", "Ksh.50.00", "yellow")
fruit_two = Fruit("Apple", "100g","Pink","Ksh.30.00", "black")
fruit_three = Fruit("Banana", "100g","Pink","Ksh.30.00")

print(fruit_three.seed_color)


# Start creating cars out of the Car class
car_one = Car("Honda", "Black", "150hp","Ksh.3,459,000")
car_two =Car("Noah","white", "1050hp","Ksh.5,379,000")
print(car_one.model)

# Start creating employees out of the Employee class
employee_one = Employee("Leah", "Female", "395648093", "Chairperson", "Ksh.645,000")
employee_two = Employee("Peter", "Male", "2578958590", "Manager", "Ksh.540,000")
employee_three = Employee("Maureen", "Female", "24664588", "Secretary", "Ksh.479.000")
employee_four = Employee("Maggy", "Female", "354776488","Treasurer", "Ksh.340,000")
print(employee_two.ID_number)

# Starting creating students out of the Student class
student_one = Student("Liam", "liamn07@gmail.com", "60085liam")
student_two = Student("Racy", "racyn08@gmail.com", "45678G")
student_three = Student("Arah", "arahcom3@gmail.com", "56327cardiow")
student_four = Student("Naicy", "naicy89@gmail.com", "673937n")
print(student_one.email)

student_one.login()
student_two.register()

# Start creating teachers out of the Teacher class
teacher_one = Teacher("King", "king@gmail.com", "King375", "Male", "Ksh 56,789")
teacher_one.register()
teacher_one.login()
teacher_one.suspend_student()

# Start creating Principals out of the Principal class
principal_one = Principal("Clinton", "clinton56@gmail.com", "cli4563", "Male", "Ksh 87,567")
print(principal_one.suspend_teacher())