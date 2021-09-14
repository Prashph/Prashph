class Employee:
    compny = "Google"
    salary = 100
harry = Employee()
rajni = Employee()
harry.salary = 300
rajni.salary = 400
# print(harry.compny)
# print(rajni.compny)
Employee.compny = "youtube"
print(harry.compny)
print(rajni.compny)
print(harry.salary)
print(rajni.salary)



