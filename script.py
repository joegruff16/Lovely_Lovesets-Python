#First inventory item
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

#Loveseat Price
lovely_loveseat_price = 254.00

#Inventory item of catalog with description using string
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

#Item price
stylish_settee_price = 180.40

#Lamp description with string
luxurious_lamp_description = "Luxurious Lamp. 36 inches tall. Brown with cream shades."

# Lamp price
luxurious_lamp_price = 52.40

#Variable to store sales tax to help us calcuate the sales tax per item
sales_tax = .088

# Tally customer purchse expenses
customer_one_total = luxurious_lamp_price + lovely_loveseat_price
#Print to ocnfirm accuracy
print(customer_one_total)

# Tally customer's purchase history descriptions
customer_one_itemization = luxurious_lamp_description + lovely_loveseat_description

#Print to confirm accuracy
print(customer_one_itemization)

#Calculate sales tax with customer total
customer_one_tax = customer_one_total * sales_tax
print(customer_one_tax)

#Calculate complete total with tax
customer_one_total = customer_one_total + customer_one_tax
print(customer_one_total)

# Create a custom receipt using Print
print("Customer One Receipt:")
print(customer_one_itemization)
print("Customer One's Total:")
print(customer_one_total)