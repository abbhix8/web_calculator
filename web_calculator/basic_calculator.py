# basic_calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def get_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculator():
    print("Welcome to the Basic Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a valid operation.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}\n")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}\n")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}\n")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}\n")

if __name__ == "__main__":
    calculator()
