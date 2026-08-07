# Print numbers till n . Get input from user 

n = int(input("Enter a number:"))
for i in range(1,n):
  print(i)
# Finding Duplicate using for loop

numbers = [1,2,3,4,3,5,2]
for i in range (len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print("duplicate",numbers[i])

# Output:
# duplicate 2
# duplicate 3
#___________________________________________________________________________________________________________________________________________________________________


# Binary search 

def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
     
        mid = left + (right - left) // 2
        
      
        if arr[mid] == target:
            return mid
      
        elif arr[mid] < target:
            left = mid + 1
    
        else:
            right = mid - 1
        
    return 0

my_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(binary_search_iterative(my_list , 5 ))

# Output:
# 1 #index value of 5 

#_____________________________________________________________________________________________________________________________________________________________________

# Get a number from user and square them 

num = int(input("Enter a number: "))
square = num * num
print("Square =", square)

# Output:
# Enter a number: 5
# Square = 25

#______________________________________________________________________________________________________________________________________________________________________


#Write a Python program to:
#Read two integers from the user.
#Swap their values.
#Print the values after swapping.
#without using if or loops 
num_1 = int(input("Enter a two digit number :"))
num_2 = int(input("Enter a two digit number:"))
print("num_1", num_2)
print("num_2", num_1)

#output:
#Enter a two digit number:25
#Enter a two digit number:45
#num_1 = 45
#num_2 = 25

#________________________________________________________________________________________________________________________________________________________________________

#Write a Python program to:
#Read an integer from the user.
#Check whether the number is even or odd.
#Print the result.

num = int(input("Enter a number :"))
if num <= 0 :
      print("Enter a valid Positive integer")
elif num%2 == 0 :
       print("The given number is even")
else:
       print("The given number is odd")

#Output :
#Enter a number: 8
# The given number is even 


#______________________________________________________________________________________________________________________________________________________________________________


#Write a Python program to:
#Read three integers from the user.
#Find the largest number.
#Print the largest number.


num_1 = int(input("Enter a number:"))
num_2 = int(input("Enter a number:"))
num_3 = int(input("Enter a number:"))

if num_1 > num_2 and num_1 > num_3:
  print("num_1 is the largest number ")
elif num_2 > num_1 and num_2 > num_3:
  print("num_2 is the largest number ")
else:
  print("num_3 is the largest number")

#output:
#Enter a number:1
#Enter a number:2
#Enter a number:3
#num_3 is the largest number 

#______________________________________________________________________________________________________________________________________________________________________________________


#Write a Python program to:
#Read a 3-digit integer from the user.
#Find the sum of its digits.
#Print the result.

num = int(input("Enter a three digit-number:"))
hundreds_digit = num // 100 
ones_digit = (num % 10) 
tens_digit = (num // 10 ) % 10 
print(res + res_2 + res_3)

#Output:
# Enter a three-digit number:123
# 6 

#___________________________________________________________________________________________________________________________________________________________________________________________

#Write a Python program to:
#read a 3-digit integer from the user.
#Reverse the digits.
#Print the reversed number.


num = int(input("Enter a three digit-number:"))
hundreds_digit = num // 100 
ones_digit = (num % 10) 
tens_digit = (num // 10 ) % 10
# print(ones_digit,tens_digit,hundreds_digit) # with space inbetween 
reverse = ones_digit * 100 + tens_digit * 10 + hundreds_digit
print(reverse)
#Output:
#Enter a three-digit number: 123
#321

#_____________________________________________________________________________________________________________________________________________________________________________________________

#Question: Count the Number of Digits
#Write a Python program to:
#Read an integer from the user.
#Count how many digits are present in the number.
#Print the total number of digits.


num = int(input("Enter a number greater than 0 :"))
count = 0

if num == 0:
    count = 1

while num > 0:
    count += 1        
    num = num // 10  

print("Total digits:", count)

#Output:
#Enter a number greater than 0 : 234
#Total digits 3

#_________________________________________________________________________________________________________________________________________________________________________________________________
#sum off all the digits using while loop

num = int(input("Enter a number: "))
total = 0
# Handle negative numbers
if num < 0:
    num = -num

# Handle the case when the number is 0
if num == 0:
    total = 0
#By getting the last digit
while num > 0:
    last_digit = num % 10
    total += last_digit
    num = num // 10

print("Sum of digits:", total)


#output:
#Enter a number: 145
#10
#___________________________________________________________________________________________________________________________________________________________________________________________________


#Write a Python program to:
#Read an integer from the user.
#Reverse its digits.
#Print the reversed number.



num = int(input("Enter a number: "))

# Handle negative numbers
if num < 0:
    num = -num

reverse = 0

# Reverse the number
while num > 0:
    last_digit = num % 10
    reverse = reverse * 10 + last_digit
    num = num // 10

print("Reversed number:", reverse)

#Output:
#Enter a number : 34
#43

#_________________________________________________________________________________________________________________________________________________________________________________


# A palindrome number is a number that reads the same forwards and backwards.
#Write a Python program to:

#Read an integer from the user.
#Reverse the number without converting it to a string.
#Compare the reversed number with the original number.
#Print:
#"Palindrome" if they are equal.
#"Not a Palindrome" otherwise.

num = int(input("Enter a number: "))

original_number = num
reverse = 0

while num > 0:
    last_digit = num % 10
    reverse = reverse * 10 + last_digit
    num = num // 10

if original_number == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
# Output:
#Enter a number : 121
#Palindrome 
#enter a number : 123
#Not a Palindrome

#_____________________________________________________________________________________________________________________________________________________________________________________________


#Check Whether a Number is an Armstrong Number (3-Digit)
#An Armstrong number is a 3-digit number in which the sum of the cubes of its digits is equal to the original number.

num = int(input("Enter a number :"))
original_num = num
sum = 0 
while num > 0 :
    last_digit = num % 10 
    total = last_digit ** 3 
    sum = sum + total 
    num = num//10
if sum == original_num :
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
#Output:
#Enter a number: 153
#Armstrong Number
#Enter a number: 123
#Not Armstrong Number 

#________________________________________________________________________________________________________________________________________________________________________________________________________


#Question: Find the Largest Digit in a Number
#Write a Python program to:
#Read an integer from the user.
#Find the largest digit present in the number.
#Print the largest digit.

num = int(input("Enter a number :"))
largest = 0 
while num > 0 :
    last_digit = num % 10 
    num = num//10
    if last_digit > largest:
        largest = last_digit
print(largest)

#Output: Enter a number : 789
#9

#________________________________________________________________________________________________________________________________________________________________________________________________________


#Question: Count the Number of Even and Odd Digits
#Write a Python program to:
#Read an integer from the user.
#Count how many even digits are present.
#Count how many odd digits are present.
#Print both counts.

num = int(input("Enter a number:"))
odd = 0
even = 0

while num > 0:
    last_digit = num % 10
    num = num // 10

    if last_digit % 2 != 0:
        odd = odd + 1
    else:
        even = even + 1

print(odd)
print(even)

#Output:
#Enter a number: 445
#1
#2

#_________________________________________________________________________________________________________________________________________________________________________________________________________

#Find the Smallest Digit in a Number
#Write a Python program to:
#Read an integer from the user.
#Find the smallest digit present in the number.
#Print the smallest digit.

num = int(input("Enter a number:"))
Lowest_number = num

while num > 0:
    last_digit = num % 10
    num = num // 10

    if last_digit < Lowest_number:
        Lowest_number = last_digit

    print(Lowest_number)

#Output:
#Enter a number:2431
#1

#_________________________________________________________________________________________________________________________________________________________________________________________________________

#Write a Python program to:
#Read an integer from the user.
#Reverse its digits.
#Print the reversed number.

num = int(input("Enter a number:"))
reverse = 0

while num > 0:
    last_digit = num % 10
    num = num // 10
    reverse = reverse*10 + last_digit
print(reverse)

#Output:
#Enter a number:123
#321

#________________________________________________________________________________________________________________________________________________________________________________________________________

#Write a Python program to:
#Read an integer from the user.
#Find the sum of all its digits.
#Print the sum.

num = int(input("Enter a number:"))
sum_digit = 0

while num > 0:
    last_digit = num % 10
    num = num // 10
    sum_digit += last_digit
print(sum_digit)
#Output:
#Enter a number : 145
#10

#_______________________________________________________________________________________________________________________________________________________________________________________________________


#Leap Year 

num = int(input("Enter a year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap year.")

#Output:
#Enter a year:2024
#2024 is a leap year.

#_____________________________________________________________________________________________________________________________________________________________________________________________________

# Question: Product of the Digits of a Number
# Write a Python program to:
# Read an integer from the user.
# Find the product of all its digits.
# Print the product.


num = int(input("Enter a number:"))
product_digit = 1

while num > 0:
    last_digit = num % 10
    num = num // 10
    product_digit *= last_digit
print(product_digit)

#Enter a number : 25
#10

#___________________________________________________________________________________________________________________________________________________________________________________________________


# Question: Count the Number of Zeros in a Number
# Problem Statement
# Write a Python program to:
# Read an integer from the user.
# Count how many digits are 0.
# Print the total number of zeros.


num = int(input("Enter a number:"))
Zero = 0
while num > 0:
    last_digit = num % 10
    num = num // 10
    if last_digit == 0:
            Zero += 1 
print(Zero)


#Enter a number : 1008
#2

#____________________________________________________________________________________________________________________________________________________________________________________________________
