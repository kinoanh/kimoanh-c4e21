items=[8,9,10,-1,3,2,5]
x=int(input("enter a number"))
if x in items:
    print("found")
    y=items.index(x)
    print(y)
else:
    print("not found")
    