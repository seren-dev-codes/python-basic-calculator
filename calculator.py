while True:
    print("----- Menu -----")
    print(""" 1.Addition 
 2.Subtraction 
 3.Multiplication 
 4.Division 
 5.Exit""")

    operation = input("Please select an operation (Press 5 to exit): ")

    if operation == "5":
        print("Program terminated.")
        break

    if operation in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == "1":
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif operation == "2":
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif operation == "3":
            print(f"Result: {num1} x {num2} = {num1 * num2}")
        elif operation == "4":
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid selection!")

print("Goodbye...")
