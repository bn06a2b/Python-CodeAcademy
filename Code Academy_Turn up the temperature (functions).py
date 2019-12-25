train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

#create function which converts fahrenheit into celsius

def f_to_c(f_temp):
  c_temp= (f_temp-32)* 5/9
  return c_temp

#convert fahrenheit to celsius when fahrenheit is 100 F
f100_in_celsius= f_to_c(100)
print(f100_in_celsius)


#create function which converts celsius to fahrenheit

def c_to_f(c_temp):
  f_temp2= c_temp* (9/5) + 32
  return f_temp2

c0_in_fahrenheit=c_to_f(0)
print(c0_in_fahrenheit)

#calculate force function

def get_force(mass,acceleration):
  force= mass * acceleration
  return force

# calculate train force using train mass and train acceleration variables- these variables have assigned values which are then input into the get_force funcion as values- this is why it works
train_force= get_force(train_mass,train_acceleration)
print(train_force)

#print the string which states the force of the train

print("The GE rain supplies "+ str(train_force) + " Newtons of force")

#Create energy equation
c= 3*10**8
def get_energy(mass,c):
  return mass * (c**2)

#calculate the energy of a 1kg bomb and print result
bomb_energy=get_energy(bomb_mass,c)
print("A 1 kg bomb supplies " + str(bomb_energy) + " Joules")


#Create a function called get_work

def get_work (mass,acceleration, distance):
  work= get_force(mass,acceleration) * distance
  return work

#calculate the amount of work the train does and put into a string. Again train_mass, train_acceleration and train_distance are all numerical values which can be input into the get_work function

train_work= get_work(train_mass,train_acceleration,train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")