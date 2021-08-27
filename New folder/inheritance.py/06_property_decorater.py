class Employee:
    company = "Bharat Gas"
    salary = 6000
    salarybonas = 300
    #tatalsalary = 6500

    @property
    def totalSalary(self):
        return self.salary + self.salarybonas
    @totalSalary.setter
    def totalSalary(self,val):
        self.salary = val - self.salarybonas

e = Employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.salarybonas)









