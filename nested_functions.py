def calculator():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    def add(x, y):
        return x + y

    def minus(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y

    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return minus(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)

result = calculator()
print("Result:", result)