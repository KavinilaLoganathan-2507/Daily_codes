# Getting three digit number and printing 10's digit
num = int(input("Enter a three digit number:"))
result = num % 100
result_2 = result // 10 
print("The result is :",result_2)
