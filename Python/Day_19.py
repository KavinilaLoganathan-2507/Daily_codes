/* Get a two-digit number from user and make the one’s digit as 0, then print it. 
Input: 95 Output 90. 
Input: 18 Output: 10
*/

num = int(input("Enter a two digit number:"))
num_2 = 0
first_num = num // 10
change_num = first_num * 10 
print("Output:", change_num)
