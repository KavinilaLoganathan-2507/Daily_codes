# Get a three-digit number from the user and subtract 5 from that number
# if the one's digit and hundred's digit are the same.


num = int(input("Enter 3 Digit Number: "))

hundred_place = (num // 100) % 10
tens_place = (num // 10) % 10   
ones_place = num % 10

result = num - 5 if ones_place == hundred_place else num

print("Output:", result)
