#take two number from user and print (sum,div,product,differnce)
num1=int(input("please enter your first number:"))
num2=int(input("please enter your second number:"))
print(f"The sum of the two number is {num1+num2}")
print(f"The substraction of the two number is {num2-num1}")
print(f"The product of the two number is {num1*num2}")
print(f"The division of the two number is {num2/num1}")

if num1>num2:
    print(f"first number{num1} is greater second number {num2}")
else:
    print(f"second number {num2} is greater first number {num1}")

