n=int(input("Enter the number: "))
odd=0
even=0
while n>0:
    d=n%10
    if d%2==0:
        even+= 1
    else:
        odd+= 1
    n=n//10
print("Even digits:", even)
print("Odd digits:", odd)