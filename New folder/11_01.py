class Programmer:
    company = "Microsoft"

    def __init__(self,name,product):
        self.name = name
        self.product = product
    def getinfo(self):
        print(f"the name of a the {self.company} progeammer {self.name} and the product is {self.product}")

prashant = Programmer("prashant","Skype")
alka = Programmer("alka","Github")
prashant.getinfo()
alka.getinfo()


