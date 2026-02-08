#Getting three digit number and printing their sum of the digits
num = int(input("Enter a three digit number:"))
result = num // 100
result_1 = num%10
result_2 = num%100
result_3 = result_2//10
Final_result = result + result_1 + result_3
print("The final result is :",Final_result)
