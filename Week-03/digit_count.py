num=int(input("enter the NUmber: "))
digits=1
while(num>9):
    num=num//10
    digits +=1
print(digits)