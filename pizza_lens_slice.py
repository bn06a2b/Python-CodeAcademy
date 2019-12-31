#addding toppings list

toppings=['pepperoni','pineapple','cheese','sausage','olives','anchovies','mushrooms']

#adding corresponding price list

prices=[2,6,1,3,2,7,2]

#number of pizzas and printing string to show no. of pizzas

num_pizzas=len(toppings)

print("We sell " +str(num_pizzas) + " different kinds of pizza!")

#combining toppings and prices into one list called pizzas and print output

pizzas=list(zip(prices,toppings))
#print(pizzas)

#sort the pizza prices from lowest to highest and update the list

prices.sort()
pizzas.sort()
print(pizzas)

#creating the cheapest pizza and most expensive pizza variables
cheapest_pizza=pizzas[0]
priciest_pizza=pizzas[-1]

#obtain the 3 lowest cost pizzas and display
three_cheapest=pizzas[:3]
print(three_cheapest)

num_two_dollar_slices=prices.count(2)
print(num_two_dollar_slices)
