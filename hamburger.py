#Description:
#Authors:
#   Christian Breshears, Jeremy Abbott, Andres Nino
from random import randrange

# Create an Order class
# constructor that defines an instance variable called burger_count
# method called randomBurgers that returns a number between 1 and 20
# constructor should call the randomBurgers() method and assign the return value to the burger_count 
#   instance variable

class Order():
  def __init__(self):
    self.burger_count = self.randomBurgers()
    print(self.burger_count)
  
  def randomBurgers(self):
    return randrange(1,21)
  

#Create a Person class
#Create a constructor that defines an instance variable called customer_name
#Create a method called randomName() that contains a list of 9 names:

#Person constructor should call the randomName() method
#and assign the return value to the customer_name instance variable
class Person():
  def __init__(self):
    self.customer_name = self.randomName()

  def randomName(self):
    asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
    return asCustomers[randrange(0,10)]


#Create a Customer class that inherits from the Person class
#Create a constructor that calls the parent constructor
#Create an instance variable called order in the constructor that is 
#  assigned an order object
class Customer(Person):
  def __init__(self):
    super().__init__()
    self.order = Order()
