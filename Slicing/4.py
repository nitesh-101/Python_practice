s=input("Enter the value: ")
if s[0].isupper():
    print("Starts with upper case")
elif s[-1].islower():
    print("Ends with lower case")
else:
    print("Other cases")