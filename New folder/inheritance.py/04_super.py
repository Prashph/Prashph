class Person:
    country = "India"

    def __init__(self):
        super().__init__()
        print("Initilizing Person.....\n")
        
    def takeBreath(self):
        print("I am breathing")

class Employee(Person):
    compny = "Hero"

    def __init__(self):
        super().__init__()
        print("Initilizing Employee.....\n")
        
    def getSalary(self):
        print(f"Salary is {self.salary}")
          
    def takeBreath(self):
        super().takeBreath()
        print("I am a Employee , so I am luckily brething")

class Programmer(Employee):
    compny = "Honda"

    def __init__(self):
        super().__init__()
        print("Initilizing Programmer.....\n")
        

    def getSalary(self):
        print("No salary for the Programmers.")

    def takeBreath(self):
        super().takeBreath()
        print("I am a Programmer , so I am luckily brething++....")


# p = Person()
# p.takeBreath()
# e = Employee()
# e.takeBreath()
pr = Programmer()
# pr.takeBreath()
print(pr.country)






