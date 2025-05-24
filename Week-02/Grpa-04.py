# Multi-purpose application
import math

# Get the operation name
operation = input()

if operation == "odd_num_check":
    number = int(input())
    if number % 2 != 0:
        print("yes")
    else:
        print("no")

elif operation == "perfect_square_check":
    number = int(input())
    sqrt_num = int(math.sqrt(number))
    if sqrt_num * sqrt_num == number:
        print("yes")
    else:
        print("no")

elif operation == "vowel_check":
    text = input()
    vowels = "aeiouAEIOU"
    has_vowel = False
    for char in text:
        if char in vowels:
            has_vowel = True
            break
    if has_vowel:
        print("yes")
    else:
        print("no")

elif operation == "divisibility_check":
    number = int(input())
    divisible_by_2 = (number % 2 == 0)
    divisible_by_3 = (number % 3 == 0)
    
    if divisible_by_2 and divisible_by_3:
        print("divisible by 2 and 3")
    elif divisible_by_2:
        print("divisible by 2")
    elif divisible_by_3:
        print("divisible by 3")
    else:
        print("not divisible by 2 and 3")

elif operation == "palindrominator":
    text = input()
    # Join string with its reverse, avoiding duplicate of last character
    reversed_text = text[::-1]
    result = text + reversed_text[1:]  # Skip first char of reversed to avoid duplication
    print(result)

elif operation == "simple_interest":
    principal_amount = int(input())
    n_years = int(input())
    
    if n_years < 10:
        interest_rate = 5  # 5%
    else:
        interest_rate = 8  # 8%
    
    # Simple Interest = (Principal * Rate * Time) / 100
    simple_interest = (principal_amount * interest_rate * n_years) / 100
    result = round(simple_interest)
    print(result)

else:
    print("Invalid Operation")