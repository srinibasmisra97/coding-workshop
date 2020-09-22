var1 = int(input("Enter a number:"))
var2 = int(input("Enter another number:"))

if var1 > var2:
    print(str(var1) + " is greater than " + str(var2))
elif var1 < var2:
    print(str(var1) + " is lesser than " + str(var2))
else:
    print(str(var1) + " is equal to " + str(var2))
