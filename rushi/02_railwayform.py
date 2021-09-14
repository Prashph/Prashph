class RailwayForm:
    formtype = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")


prashantApplication = RailwayForm()
prashantApplication.name = "prashant"
prashantApplication.train = "rajdhani express"
prashantApplication.printData()


rutujaApplication = RailwayForm()
rutujaApplication.name = "Rutuja"
rutujaApplication.train = "rajdhani express"
rutujaApplication.printData()

