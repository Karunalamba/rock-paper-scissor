#check whether a no. is palindrome or not
num= int(input("enter the number:"))
temp= num
reverse= 0

while(num>0):
    digit=num%10
    reverse= reverse*10 + digit
    num= num//10

    print(reverse)

if temp==reverse:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")