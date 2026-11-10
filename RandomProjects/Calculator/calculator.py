def main():
    print("Enter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3' for multiplication")
    print("Enter '4' for division")
    print("Enter '5' for average")

    operation = input("Choose an operation: ")
    if operation not in {"1", "2", "3", "4", "5"}:
        print("Invalid operation.")
        return

    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    if operation == "1":
        result = first_number + second_number
    elif operation == "2":
        result = first_number - second_number
    elif operation == "3":
        result = first_number * second_number
    elif operation == "4":
        if second_number == 0:
            print("Cannot divide by zero.")
            return
        result = first_number / second_number
    else:
        result = (first_number + second_number) / 2

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
