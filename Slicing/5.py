n=eval(input("Enter the list: "))
mid=len(n)//2
first=sum(n[:mid])
second=sum(n[mid:])
if first>second:
    print("First half greater")
elif first==second:
    print("Equal halves")
else:
    print("Second half greater")