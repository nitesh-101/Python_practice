s = input("Enter string: ")

if s.startswith("A"):
    if s.endswith("Z"):
        print("Valid AZ string")
    else:
        print("Starts with A but invalid end")
else:
    print("Invalid string")