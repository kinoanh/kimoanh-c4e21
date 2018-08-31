items=[8,9,10,-1,3,2,5,]
x=int(input("enter a number"))
found=False
for index, item in enumerate(items):
    if x== item :
        found=True
        print("found!")
        print(index)
        break #findone
#if found == False: #if not found :
    #print("not found")
else:
    print("not found")