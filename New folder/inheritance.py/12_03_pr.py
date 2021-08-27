class Employee:
    salary = 200
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sal):
        self.increment = sal/self.salary

e = Employee()
print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement = 400
print(e.increment)


