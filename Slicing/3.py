s=input("Enter the value: ")
last=s[-1]
if last.isdigit():
    print("Ends with digits")
elif last.isalpha():
    print("Ends with char")
else:
    print("Ends with special chararcter")