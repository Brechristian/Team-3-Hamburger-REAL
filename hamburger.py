#Description:
#Authors:
#   Christian Breshears, Jeremy Abbott
#Test
from random import randrange

class Order():
  def __init__(self):
    self.burger_count = self.randomBurgers()
    print(self.burger_count)
  def randomBurgers(self):
    return randrange(1,21)
  
class Person():
  def __init__(self):
    self.customer_name = self.randomName()

  def randomName(self):
    asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
    return asCustomers[randrange(0,10)]

class Customer(Person):
  def __init__(self):
    super().__init__()
    self.order = Order()
