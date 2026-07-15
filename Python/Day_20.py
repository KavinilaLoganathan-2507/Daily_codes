# Get a two-digit number from user and make the ten’s digit 1, then print it.

num = int(input("Enter two digit number :"))
result = num % 10 + 10 
print("Output : ",result)
