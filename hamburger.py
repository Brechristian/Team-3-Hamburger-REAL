#Description:
#Authors:
#  Christian Breshears, Jeremy Abbott , Andres F. Nino, Sawyer Evans

from random import randrange

# Create an Order class
# constructor that defines an instance variable called burger_count
# method called randomBurgers that returns a number between 1 and 20
# constructor should call the randomBurgers() method and assign the return value to the burger_count 
#   instance variable

class Order():
  def __init__(self):
    self.burger_count = self.randomBurgers()
    
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
    return asCustomers[randrange(0,9)]


#Create a Customer class that inherits from the Person class
#Create a constructor that calls the parent constructor
#Create an instance variable called order in the constructor that is 
#  assigned an order object
class Customer(Person):
  def __init__(self):
    super().__init__()
    self.order = Order()

#Create a variable for a Queue that will be assigned items of type Customer
lineCustomers = []


#Create a variable for a Dictionary with keys of type string and values of type int.
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

#Put 100 customers into the queue.
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






