#Get a four-digit number from user and only reverse the first two digits of the number, then print the number.

num = int(input("Enter four-digit number: "))

# Extract digits
thousand = (num % 10000) // 1000
hundred = (num % 1000) // 100
tens = (num % 100) // 10
ones = num % 10

# Logic (reverse last two digits)
first_two = thousand * 1000 + hundred * 100
last_two = ones * 10 + tens

result = first_two + last_two

print("Output:", result)
