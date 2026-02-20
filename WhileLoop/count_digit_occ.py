#count how many times a specific digit appears in a number
n=input("Enter the number: ")
s=input("Enter the number to search: ")
l=len(str(n))
c=0
i=0
while(i!=l):
    if((s)==n[i]):
        c+=1
    i+=1
print(c)