num = int(input("Enter a number: "))
original=num
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print("Reversed number:", reverse)
if reverse>original:
    print("Reversed number is greater than original")
elif reverse<original:
    print("Reversed number is smaller than original")
else:
    print("Both numbers are equal")