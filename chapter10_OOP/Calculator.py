import math
class Calculator:

    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"The square is {self.n*self.n}")
    
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {math.sqrt(self.n)}")

a=Calculator(4)
a.square()
a.cube()
a.squareroot()