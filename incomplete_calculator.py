def add(num1, num2):
    return num1 + num2


if __name__ == "__main__":
    while True:
        print("----------------------------")
        print("1. Add.")
        print("2. Subtract.")
        print("3. Multiply.")
        print("4. Divide.")
        print("5. Exit.")
        choice = int(input("Enter your choice:"))

        if choice > 5:
            print("Please enter a valid input!")
            continue
        elif choice == 5:
            print("Goodbye!")
            break

        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))

        if choice == 1:
            result = add(num1, num2)

        print("Result: " + str(result))
