class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    

    def introduce(self):
        print("Hi, I am " + self.name + ", age " + str(self.age))


s1 = Student("Athira", 31)
s2 = Student("Sreejith", 36)

s1.introduce()
s2.introduce()
print(s1.name)


class Employee:
    def __init__(self, name, exp, designation):
        self.name = name
        self.exp = exp
        self.designation = designation

    def show_details(self):
        print("Hi, I am " + self.name + ", exp " + str(self.exp) + ", designation " + self.designation)

    def is_senior(self):
        return self.exp > 5

e1 = Employee("Athira", 5, "Software Engineer")
e2 = Employee("Sreejith", 10, "Senior Software Engineer")

e1.show_details()
e2.show_details()
print(e1.is_senior())
print(e2.is_senior())




