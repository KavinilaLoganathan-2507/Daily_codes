# Get a three-digit number from user and print the reverse of the number

num = int(input("Enter a 3-digit number: "))
digit_1 = num//100
digit = num%100
digit_2 = digit//10
digit_3 = num%10
reverse = (digit_3*100)+(digit_2*10)+digit_1
print("Reversed number:", reverse)
