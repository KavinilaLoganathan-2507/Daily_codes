# Get a three-digit number from the user and make the ten's digit 0
# Input: 695 -> Output: 605
# Input: 182 -> Output: 102

num = int(input("Enter a three-digit number: "))

hundreds_place = (num % 1000) // 100
tens_place = (num % 100) // 10   
ones_place = num % 10

result = (hundreds_place * 100) + ones_place

print("Output:", result)
