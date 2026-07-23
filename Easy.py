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
