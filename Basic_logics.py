# Get a number from ussr and print
num = int(input("Enter a number :"))
print(num)
#Get a array from user and print 
arr = list(map(int , input("Enter spaced values :").split()))
print(arr)
# Accessing each element 
for i in arr:
#Adding 1 element in each values
  i += 1
  print(i)
#Subtracting 1 in each element 
  i -= 1
  print(i)
#positive index = goes from left to right
print(arr[1])
#negative index = goes from right to left 
print(arr[-1])
#delete an element in a given array
#---------------------------------#
## Using in-bult function ##
arr = [1, 2 , 3]
#Using list slicing
arr = arr[1:]
print(arr)  
#using pop and delete 
arr = [2 , 4 ,5]
del arr[0]
arr.pop(0)
print(arr)
##------------------------------#
## Without using Built-in function ##

arr = list(map(int , input("Enter spaced values :").split()))
del_value = int(input("Enter the value to delete: "))

new_arr = []
for i in arr:
    if i != del_value:
        new_arr += [i]  

print(new_arr)

#---------------------------------------#

##Insert##
##Search & Sort ##


