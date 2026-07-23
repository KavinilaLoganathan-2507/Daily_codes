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

# Binary search 

def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
     
        mid = left + (right - left) // 2
        
      
        if arr[mid] == target:
            return mid
      
        elif arr[mid] < target:
            left = mid + 1
    
        else:
            right = mid - 1
        
    return 0

my_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(binary_search_iterative(my_list , 5 ))
