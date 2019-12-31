def cost_of_ground_shipping(weight):
  if weight <=2:
    return (1.5* weight)  + 20
    
  elif weight <=6:
    return (3* weight)+ 20
     
  elif weight <=10:
    return (4*weight) + 20
  
  elif weight >10:
    return (4.75*weight)+ 20
    
 
print(cost_of_ground_shipping(8.4))

cost_of_premium_shipping= 125


def cost_of_drone_shipping(weight):
  if weight <=2:
    return (4.5 * weight) 
    
  elif weight <=6:
    return (9 * weight)
     
  elif weight <=10:
    return (12 *weight)
  
  elif weight >10:
    return (14.25 *weight)
  
print(cost_of_drone_shipping(1.5))

def cheapest_shipping(weight):
  
  cost_of_ground_shipping(weight)
  cost_of_drone_shipping(weight)
  cost_of_premium_shipping
  
  if cost_of_ ground_shipping(weight)< cost_of_drone_shipping(weight) and cost_of_ ground_shipping(weight) < cost_of_premium_shipping:
    print("You should ship by ground") 
  elif cost_of_drone_shipping(weight) < cost_of_ ground_shipping(weight) and cost_of_drone_shipping(weight) < cost_of_premium_shipping:
    print("You should ship by drone")
  
  else:
    print("You should ship by premium")