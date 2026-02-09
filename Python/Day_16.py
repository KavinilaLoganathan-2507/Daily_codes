# Get atwo digit number and print their reverse
num = int(input("Enter a two digit number:"))
result = num % 10
result_1 = num // 10
result_2 = result * 10 + result_1
print("The finale result is :", result_2)
