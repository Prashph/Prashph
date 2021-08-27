class Calculater:
    def __init__(self,num):
        self.num = num
    
    def square(self):
       print(f"the value of {self.num} square is {self.num**2}")

    def squareRoot(self):
       print(f"the value of {self.num} squareRoot is {self.num**0.5}")


    def cube(self):
      print(f"the value of {self.num} cube is {self.num**3}")

    @staticmethod
    def greet():
        print("****welcome****")


a = Calculater(9) 
a.greet()
a.square()     
a.squareRoot()
a.cube()

