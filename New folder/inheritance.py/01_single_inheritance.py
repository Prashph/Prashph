class Employee:
    compny = "Google"

    def showDetails(self):
        print("This is an Employee")

class Programmer:
    language = "Python"
    compny = "Youtube"
    def getLanguage(self):
        print(f"The Programmer Language is {self.language}")

    def showDetails(self):
        print("This is an Programmer")

e = Employee()
p = Programmer()
e.showDetails()
p.getLanguage()
p.showDetails()
print(p.compny)






