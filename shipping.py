#shipping.py --takes the weight of a package and determine
#the cheapest way to ship that package
#Part of Codecademy/CS track
def ground_shipping(weight):
 if weight <= 2:
  cost = weight*1.5+20
 elif weight <= 6:
  cost = weight*3+20
 elif weight <= 10:
  cost = weight*4+20
 else:
  cost = weight*4.75+20
 return cost

premium_ground_shipping = 125
print(ground_shipping(8.4))

def drone_shipping(weight):
 if weight <= 2:
  cost = weight*4.5
 elif weight <= 6:
  cost = weight*9
 elif weight <= 10:
  cost = weight*12
 else:
  cost = weight*14.25
 return cost

print(drone_shipping(1.5))

def cheapest_shipping(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight)< premium_ground_shipping:
    return "You should ship ground shipping. it will cost $" + ground_shipping(weight)
  if drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_ground_shipping:
    return "You should ship drone shipping. it will cost $" + drone_shipping(weight)
  if premium_ground_shipping < ground_shipping(weight) and premium_ground_shipping < drone_shipping(weight):
    return "You should ship premium ground. it will cost $" + premium_ground_shipping
	
