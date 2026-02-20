s = input("Enter string: ")

if s[:2].isdigit():
    if s[-2:].isalpha():
        print("Valid format")
    else:
        print("Invalid format")
else:
    print("Invalid format")