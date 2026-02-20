u="Admin"
p=123
i=3
while(i!=0):
    u1=input("Enter username: ")
    n=int(input("Enter password: "))
    if(n==p and u==u1):
        print("Login Success")
    elif(n!=p or u!=u1 and i!=0):
        print(i-1, "Attempt left")
    elif(i==0):
        print("login failed")
    i=i-1
