### 1
test = 85

def check_grade(score):
    if 90 <= score <= 100:
        return 'Excellent'
    elif 75 <= score <= 89:
        return 'Good'
    elif 50 <= score <= 74:
        return 'Satisfactory'
    else:
        return 'Unsatisfactory'

print(f'Score for {test} points: {check_grade(test)}.')


### 2


def is_even(number):
    return 'even' if number % 2 == 0 else 'odd'

print(f'The number 4 is {is_even(4)}.')
print(f'The number 7 is {is_even(7)}.')


### 3

first, second = 10, 20

def find_max(a, b):
    if a > b:
        return a
    else:
        return b

print(f'The maximum of the numbers {first} and {second}: {find_max(first, second)}.')


### 4


def check_number(number):
    if number > 0:
        if number % 2 == 0:
            return 'The number ' + str(number) + ' is positive and even.'
        else:
            return 'The number ' + str(number) + ' is positive.'
    else:
        return 'The number ' + str(number) + ' is negative.'

print(check_number(8))
print(check_number(-5))


### 5

test_str = 'Python'
test_hi = 'Hi'

def check_string_length(string, length):
    if len(string) > length:
        return 'The string length is sufficient'
    else:
        return 'The string is too short'

print(f'The length of the string "{test_str}" is {check_string_length(test_str, 5)}.')
print(f'The string "{test_hi}" is {check_string_length(test_hi, 5)}.')