import random
class Train:
    def __init__(self,tno):
        self.tno=tno

    def book(self,fro,to):
        print(f"Ticket is booked in train no: {self.tno} from {fro} to {to}")

    def getStatus(self):
        print(f"Ticket no: {self.tno} is running successfully")

    def getFare(self,fro,to):
        print(f"Ticket is booked in train no: {self.tno} from {fro} to {to} is {random.randint(100,150)}")


t=Train(123)
t.book("Nepal","India")
t.getStatus()
t.getFare("Nepal","India")