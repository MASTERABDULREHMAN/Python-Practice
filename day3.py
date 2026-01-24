#this is my day 3 progress 
#1-programme to check if the word is pallindrome or not
# def pallin(name):

#     reversed=""
#     for i in range(len(name)-1,-1,-1):
#      reversed=reversed+name[i]
#     if reversed==name:
#        print("yes")
#     else:
#        print("no")
# pallin("abdulrehman")
# pallin("NAN")


#2-programme to count digits in numbers


def count_digits(n):
    n = abs(n)          # remove negative sign
    if n == 0:
        return 1

    count = 0
    while n > 0:
        n = n // 10     # remove last digit
        count += 1

    return count
count_digits(1234567)