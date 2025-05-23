num = input("Enter a number: ")

# Check if input is a valid integer (including negative numbers)
if num.lstrip('-').isdigit():
    last_digit = num[-1]
    
    if last_digit == '5':
        print("Entered Number ends with 5")
    elif last_digit == '0':
        print("Entered Number ends with 0")
    else:
        print("Entered Number does not end with either 0 or 5")
else:
    print("Invalid input. Please enter a valid integer.")