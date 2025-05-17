# Input values (will be changed by the autograder)
a = 5
b = 6

# Calculate and print the sum of a and b
sum_ab = a + b
print(sum_ab)  # int: sum of a and b

# Calculate and print twice the sum of a and b
twice_sum = 2 * sum_ab
print(twice_sum)  # int: twice the sum of a and b

# Calculate and print the absolute difference between a and b
abs_diff = abs(a - b)
print(abs_diff)  # int: absolute difference between a and b

# Calculate and print the absolute difference between sum and product of a and b
abs_sum_product_diff = abs(sum_ab - (a * b))
print(abs_sum_product_diff)  # int: absolute difference between sum and product

# Find discounted price given price and discount_percent
price = 80
discount_percent = 2

# Calculate discounted price
discount_amount = (discount_percent * price) / 100
discounted_price = price - discount_amount
print(discounted_price)  # float: discounted price

# Round the discounted price to the nearest integer
rounded_discounted_price = round(discounted_price)
print(rounded_discounted_price)  # int: rounded discounted price

# Convert total minutes into hours and minutes
total_mins = 270
hrs = total_mins // 60  # Floor division gives hours
mins = total_mins % 60  # Modulo gives remaining minutes
print(hrs)  # int: hours
print(mins)  # int: minutes
