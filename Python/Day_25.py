# Get a two-digit number from the user and subtract 5 if the sum of its digits is odd.
# Do not use "if".

n = int(input("Enter 2 digit number: "))

tens_digit = (n // 10) % 10
ones_digit = n % 10

result = n if ((tens_digit + ones_digit) & 1) == 0 else n - 5

print("Output:", result)
