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

#Write a Python program that:
# Takes an integer as input.
# Takes another digit from the user.
# Counts how many times that digit appears in the number.
# Prints the count.

num_1 = int(input("Enter a number :"))
num_2 = int(input("Enter a digit :"))
count = 0
while num_1 > 0:
    last_digit = num_1 % 10
    num_1 = num_1 // 10
    if num_2 == last_digit:
        count = count + 1
print(count)

#Output:
#Enter a number: 151
#Enter a digit :1
# 2

#_________________________________________________________________________________________________________________________________________________________________________________________________


# Write a Python program to:
# Take an integer as input.
# Find the largest digit present in the number.
# Print the largest digit.

num_1 = int(input("Enter a number :"))
largest_number = 0
while num_1 > 0:
    last_digit = num_1 % 10
    num_1 = num_1 // 10
    if last_digit > largest_number:
        largest_number =  last_digit
print(largest_number)

#Output:
#Enter a number:189
#9

#__________________________________________________________________________________________________________________________________________________________________________________________________

# Write a Python program to:
# Take an integer as input.
# Check whether the number is a prime number.
# Print whether it is prime or not.

num = int(input("Enter a number :"))
if num <= 1:
    print(num, "is not a prime number")
else:
    for i in range(2, num): #(2,(num**0.5) +1)
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

  #Output:
  #Enter a number: 5
  #is a prime number

#____________________________________________________________________________________________________________________________________________________________________________________________________


#Write a Python program to:
# Take an integer as input.
# Find the smallest digit present in the number.
# Print the smallest digit.

num = int(input("Enter a number :"))
smallest_number = num
while num > 0:
  last_digit = num % 10
  num = num //10
  if last_digit < smallest_number :
    smallest_number = last_digit
print(smallest_number)

#Output: Enter a number: 145
#1 
#_____________________________________________________________________________________________________________________________________________________________________

# Write a Python program that:
# Takes a positive integer as input.
# Calculates its factorial.
# Prints the result.
# The factorial of a number n
#n × (n-1) × (n-2) × ... × 2 × 1

num = int(input("Enter a number:"))
factorial_number = 1
for i in range(1, num+1):
    factorial_number = factorial_number * i
print(factorial_number)

#Output: Enter a number:6
#720

#________________________________________________________________________________________________________________________________________________________________________


# Write a Python program that:
# Takes an integer as input.
# Counts how many digits are present in the number.
# Prints the total number of digits.

num = int(input("Enter a number :"))
count_num = 0
while num >0:
    last_digit = num % 10
    num = num // 10
    if num >= 0:
        count_num += 1

print(count_num)

#Output: Enter a number: 145
#3

#________________________________________________________________________________________________________________________________________________________________________

# Write a Python program that:
# Takes a positive integer N as input.
# Calculates the sum of all natural numbers from 1 to N.
# Prints the result.

num = int(input("Enter a number N:"))
total_sum = 0
for i in range(1,num+1):
    total_sum += i  
print(total_sum)     

#Output: Enter a number N:6
#21

#__________________________________________________________________________________________________________________________________________________________________________

# Write a Python program that:
# Takes a word or sentence as input.
#Print how many letters are there


wrd = input("Enter a string:")
total_count = 0
for i in wrd:
    total_count += 1
print(total_count)

#Output: Enter a string: vino
#4

#__________________________________________________________________________________________________________________________________________________________________________________

#Get a string
# Counts how many vowels it contains.
# Prints the total number of vowels.

wrd = input("Enter a string:")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E','I','O', 'U'] 
total_count = 0
for i in wrd:
    if i in vowels :
        total_count += 1
print(total_count)

#Output: Enter a string: good
#2

#_________________________________________________________________________________________________________________________________________________________________________________


# Write a Python program that:
# Creates a list of integers.
# Finds the largest number in the list.
# Prints the largest number.

arr = list(map(int, input("Enter space-separated numbers: ").split()))

largest_number = arr[0]

for i in arr:
    if i > largest_number:
        largest_number = i

print("Largest number:", largest_number)

#Output: Enter space-separated numbers: 1 4 8 2
#Largest number: 8

#_____________________________________________________________________________________________________________________________________________________________________________________________


# Write a Python program that:
# Takes a list of integers from the user.
# Counts how many numbers are even.
# Counts how many numbers are odd.
# Prints both counts.

arr = list(map(int, input("Enter spaced numbers:").split()))
even_count = 0
odd_count = 0
for i in arr:
    if i%2 == 0:
        even_count += 1
    else:
        odd_count += 1 
print("odd:",odd_count)
print("even:",even_count)

#Output: Enter spaced numbers: 1 2 3 4
#odd:2
#even:2

#______________________________________________________________________________________________________________________________________________________________________________________________________

# Write a Python program that:
# Takes a list of integers from the user.
# Finds the second largest distinct number.
# Prints it.

arr = list(map(int, input("Enter spaced numbers: ").split()))

largest = arr[0]
second_largest = 0

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num

    elif num != largest and (second_largest is 0 or num > second_largest):
        second_largest = num

print("Second_largest:", second_largest)
print("Largest:", largest)

#Output: Enter spaced numbers:1 2 3
#Second_largest: 2
#Largest: 3

#________________________________________________________________________________________________________________________________________________________________________________________________________

#Fibonacci

num = int(input("Enter a number :"))
a, b = 0, 1

for i in range(0, num):
    print(a, end=" ")  # 1. Print the current number 'a'
    a, b = b, a + b    # 2. Move to the next numbers

#Output: Enter a number : 3
#0 1 1 

#_________________________________________________________________________________________________________________________________________________________________________________________________


#Remove Duplicates from a List
# Input:
# 10 20 10 30 20 40 30

# Output:
# [10, 20, 30, 40]

arr = list(map(int, input("Enter the spaced numbers: ").split()))

unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print(unique)

#________________________________________________________________________________________________________________________________________________________________________________________________________________________

#Count Frequency of Each Number
# Takes a list of integers from the user.
# Finds how many times each number appears.
# Prints each number along with its frequency.
# Keeps the order in which each number first appeared.

arr = list(map(int, input("Enter spaced numbers: ").split()))

frequencies = {}
for num in arr:
    if num in frequencies:
        frequencies[num] += 1
    else:
        frequencies[num] = 1

for num, count in frequencies.items():
    print(f"{num}:{count}")

#Output: Enter spaced numbers: 10 10 20 30
#10 : 2
#20 : 1
#30 : 1

#________________________________________________________________________________________________________________________________________________________________________________________________

#Find the First Non-Repeating Character
# Takes a string from the user.
# Finds the first character that appears only once in the string.
# Prints that character.
# If every character repeats, print "No unique character".

# Example 

# Input:

# aabbcde

# Output:

# c

user_string = input("Enter a string: ")

for char in user_string:
    if user_string.count(char) == 1:
        print(char)
        break
else:
    print("No unique character")
#____________________________________________________________________________________________________________________________________________________________________________________________________
