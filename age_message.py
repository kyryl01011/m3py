birth_year = int(input("Enter your birth year: "))
age = 2025 - birth_year
if age < 18:
    print("You are still young, learning is your path!")
elif 18 <= age <= 65:
    print("Excellent age for career growth!")
else:
    print("It's time to enjoy a well-deserved rest!")