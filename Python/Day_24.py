# Get a number from the user and subtract 5 from that number
# if the number's ten's position digit is odd.
# Do not use "if".

num = int(input("Enter the number: "))

tens_position = (num // 10) % 10

result = num - 5 * (tens_position & 1)

print("Output:", result)
