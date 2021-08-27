class Employee:
    compny = "Visa"
    eCode = 120

class Freelancer:
    compny = "Fiverr"
    level = 0

    def upgradelevel(self):
        self.level = self.level + 1

class Programmer(Employee,Freelancer):
    name = "Prashant"

p = Programmer()
p.upgradelevel()
print(p.level)
print(p.compny)




