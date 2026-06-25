number1: str = input("Enter number 1: ")
print(number1)
operation: str = input("Enter operation (+, -, *, /)? ")
number2: str = input("Enter number 2: ")
print(number2)
result: float = 0.0

if operation == "+":
    result = float(number1) + float(number2)
elif operation == "-":
    result = float(number1) - float(number2)
elif operation == "*":
    result = float(number1) * float(number2)
elif operation == "/":
    result = float(number1) / float(number2)
    if float(number2) != 0:
        result = float(number1) / float(number2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation. Please use +, -, *, or /.")

print(f"{number1} {operation} {number2} = {result}")