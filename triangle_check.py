def check_triangle(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            return "The triangle is ravnostoronniy."
        elif a == b or b == c or a == c:
            return "The triangle is ravnobedrenniy."
        else:
            return "The triangle is raznostoronniy."
    else:
        return "A triangle cannot be formed."

a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))
print("Result:", check_triangle(a, b, c))