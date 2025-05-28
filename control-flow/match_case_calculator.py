first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = int(first_number) + int(second_number)
        print(f"The result is {result}")
    case "-":
        result = int(first_number) - int(second_number)
        print(f"The result is {result}")
    case "*":
        result = int(first_number) * int(second_number)
        print(f"The result is {result}")
    case "/":
        if int(second_number) == 0:
            print("Cannot divide by zero.")
        else:
            result = int(first_number) / int(second_number)
            print(f"The result is {result}")
    case _:
        print("Invalid operation. Please choose +, -, *, or /.")  # Default case if no match is found

        