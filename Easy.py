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

#___________________________________________________________________________________________________________________________________________________________________________________________________

#Let us say your expense for every month are listed below,
#January - 2200
#February - 2350
#March - 2600
#April - 2130
#May - 2190
#Create a list to store these monthly expenses and using that find out,

#1. In Feb, how many dollars you spent extra compare to January?
#2. Find out your total expense in first quarter (first three months) of the year.
#3. Find out if you spent exactly 2000 dollars in any month
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#5. You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this


monthly_expense = [2200, 2350, 2600, 2130, 2190]

# 1
print(monthly_expense[1] - monthly_expense[0])

# 2
print(sum(monthly_expense[:3])) # res = monthly_expense[0] + monthly_expense[1] + monthly_expense[2]

# 3
if 2000 in monthly_expense:
    print("Spent exactly $2000")
else:
    print("Did not spend exactly $2000")

# 4
monthly_expense.append(1980)
print(monthly_expense)

# 5
monthly_expense[3] =  monthly_expense[3] - 200 
print(monthly_expense)
