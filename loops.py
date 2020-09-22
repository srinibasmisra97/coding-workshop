print("For loop example 1:")
for i in range(10):
    print(i)

print("For loop example 2:")
for a in ['a','b','c','d','e']:
    print(a)

print("While loop example 1:")
z = 10
while z >= 0:
    print(z)
    z = z - 1

print("Infinite while loop with break example:")
z = 10
while True:
    print(z)
    if z == 3:
        print("Now breaking")
        break
    z = z - 1

print("For loop with continue example:")
for i in range(10):
    if i == 5:
        print("Skipping")
        continue
    print(i)