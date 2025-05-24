main_dish = str(input())
time_of_day = int(input())
has_voucher = False if input() == "False" else True
is_card_payment = False if input() == "False" else True

# Determine base cost
if main_dish == "paneer tikka":
    cost = 250
elif main_dish == "butter chicken":
    cost = 240
elif main_dish == "masala dosa":
    cost = 200
else:
    print("Invalid main dish")
    exit()

total_cost = cost

# Apply lunch discount
if 12 <= time_of_day <= 15:
    total_cost *= 0.85  # 15% discount

# Apply voucher discount
if has_voucher:
    total_cost *= 0.90  # 10% discount

# Apply card payment service charge
if is_card_payment:
    total_cost *= 1.05  # 5% service charge

# Final amount
print(f"{total_cost:.2f}")