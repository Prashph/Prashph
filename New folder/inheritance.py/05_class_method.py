class Employee:
    company = "Camel"
    salary = 100
    location = "pune"

    # def changeSalary(self,sal):                #1st method
    #     self.__class__.salary = sal

    @classmethod                                 #2nd method
    def changeSalary(cls,sal):
        cls.salary = sal


e = Employee()
# print(e.salary)
e.changeSalary(455)
print(e.salary)

