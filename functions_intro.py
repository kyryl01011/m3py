def greet_user(name):
    print(f"Hello, {name}! Welcome to the world of Python!")

def calculate_sum(a, b):
    return a + b

name = input("Enter your name: ")
greet_user(name)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The sum of the numbers is:", calculate_sum(num1, num2))