#This is day 2 of learning python
#today i am taking input from user check positive/negatice/zero
#and print all even numbers and print sum of that number
number=int(input("Please enter any no"))
if number==0:
    print("the number is zero")
elif number>0:
    print("the number is positive")
else:
    print("the number is negative")

#check the no is even or odd
if number%2==0:
    print("the number is even")
else:
    print("the number is odd")

#sum of the number
    total = 0
for i in range(1, number + 1):
    total += i

print("Sum:", total)
