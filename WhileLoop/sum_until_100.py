#Keep accepting number until sum excced 100
s=0
n=0
while(s<=100):
    n=int(input("Enter the number: "))
    s+=n
print("Number exceeded")
print(s-n)