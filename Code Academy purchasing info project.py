#This project creates purchasing information and receipts for a customers activity

#Adding item description, prices, sales tax and setting their initial total to zero and itemisation is blank

lovely_loveseat_description= """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white. """
lovely_loveseat_price = 254.00
stylish_settee_description= """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""
stylish_settee_price= 180.50
luxurious_lamp_description= """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade"""
luxurious_lamp_price= 52.15
sales_tax= 0.088
customer_one_total=0
customer_one_itemization=""

#Adding items to shopping list
customer_one_total+=lovely_loveseat_price
customer_one_itemization+=lovely_loveseat_description
customer_one_total+=luxurious_lamp_price
customer_one_itemization+=stylish_settee_description

#Adding sales tax to customer purchases
customer_one_tax=round(customer_one_total*sales_tax)
customer_one_total+=customer_one_tax

#printing the items they purchased and description and total price
print("Customer One Items:",customer_one_itemization," Customer One Total:", customer_one_total)