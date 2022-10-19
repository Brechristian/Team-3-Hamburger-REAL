#Description:
#Authors:
#   Christian Breshears, Jeremy Abbott , Andres F. Nino
#Test
from random import randrange

class Order():
  def __init__(self):
    self.burger_count = self.randomBurgers()
    
  def randomBurgers(self):
    return randrange(1,21)
  
class Person():
  def __init__(self):
    self.customer_name = self.randomName()

  def randomName(self):
    asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
    return asCustomers[randrange(0,9)]

class Customer(Person):
  def __init__(self):
    super().__init__()
    self.order = Order()

lineCustomers = []

infoCustomers = {}
infoCustomers ["Jefe"] = 0
infoCustomers ["El Guapo"] = 0
infoCustomers ["Lucky Day"] = 0
infoCustomers ["Ned Nederlander"] = 0
infoCustomers ["Dusty Bottoms"] = 0
infoCustomers ["Harry Flugleman"] = 0
infoCustomers ["Carmen"] = 0
infoCustomers ["Invisible Swordsman"] = 0
infoCustomers ["Singing Bush"] = 0

for x in range(100):
    lineCustomers.append(Customer())
    #print(lineCustomers[x].customer_name, lineCustomers[x].order.burger_count)
    infoCustomers[lineCustomers[x].customer_name] += (lineCustomers[x].order.burger_count)

for x in infoCustomers:
  print(x, infoCustomers[x])






# v
# #print(infoCustomers[x])









#lineCustomers = [0] * 100

#for i in range(0, len(lineCustomers)):
#     lineCustomers[i] = Customer()
#      print (lineCustomers[i])






