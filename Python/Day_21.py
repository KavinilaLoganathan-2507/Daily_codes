# Get a three-digit number from user and make the one’s digit as 2, then print it.

num = int(input("Enter a three digit number :"))

res1 = num%1000/100
res2 = num%100/10
res3 = num%10
res4 = res1 * 100
res5 = res2 * 10
fin_res = res1 + res2 + 2 

print("output",fin_res)
