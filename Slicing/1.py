n=eval(input("Enter the list: "))
if n[0:2]==n[-2:]:
    print("Valid slice")
else:
    print("Not a valid slice")