# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# This is the first line of the exercise
task = input()
# <eoi>

if task == "sum_until_0":
    total = 0
    n = int(input())
    while n>0: # the terminal condition
        total=total+n # add n to the total
        n=int(input()) # take the next n form the input
    print(total)

elif task == "total_price":
    total_price = 0
    while True: # repeat forever since we are breaking inside
        line = input()
        if line=="END": # The terminal condition
            break
        quantity, price = line.split() # split uses space by default
        quantity, price = int(quantity), int(price) # convert to ints
        total_price += price*quantity # accumulate the total price
    print(total_price)
elif task == "only_ed_or_ing":
    while True:
        word = input()
        if word == "END":
            break
        if word.endswith("ed") or word.endswith("ing"):
            print(word)



elif task == "reverse_sum_palindrome":
    while True:
        num_str = input().strip()
        if num_str == '-1':
            break
        num = int(num_str)
        reverse_num = int(num_str[::-1])
        total = num + reverse_num
        total_str = str(total)
        if total_str == total_str[::-1]:
            print(num)

elif task == "double_string":
    line = input()
    while(line != ''):
        repeatedTwice = line * 2
        print(repeatedTwice)
        line = input()



elif task == "odd_char":
    word = input()
    while(word != word.endswith('.')):
        odd_char = word[::2]
        print(odd_char, end = ' ')
        word = input()

elif task == "only_even_squares":
    num = input()
    while(num != 'NAN'):
        num = int(num)
        square = num ** 2
        if (square % 2 == 0):
            print(square)
        else:
            pass
        num = input()

elif task == "only_odd_lines":
    new_line = ''
    line = input()
    while(line != 'END'):
        new_line = new_line + line + ' '
        line = input()
    split_line = new_line.split()
    odd_line = split_line[::2]
    reverse_odd_line = odd_line[::-1]
    reversed_line = '\n'.join(reverse_odd_line)
    print(reversed_line)