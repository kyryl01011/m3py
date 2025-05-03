### 1

def sum_numbers(n):
    result = 0
    for num in range(1, n + 1):
        result += num
    return result

print(sum_numbers(5))


### 2

def find_min(n):
    lowest = n[0]
    for num in n:
        if num < lowest:
            lowest = num
    return lowest

print(find_min([3, 1, 4, 1, 5]))

### 3

def count_vowels(string):
    result = 0
    for x in string:
        if x in ['a', 'e', 'i', 'o', 'u']:
            result += 1
    return result

print(count_vowels("Hello World"))

### 4

# def print_diamond(rows): # Also works
#     for i in range(0, rows + 1):
#         print('*' * i)
#     for i in reversed(range(0, rows)):
#         print('*' * i)

def print_diamond(rows):
    reverse = False
    i = 0
    while True:
        if i < 0:
            break
        print('*' * i)
        if i == rows:
            reverse = True
        if reverse:
            i -= 1
        else:
            i += 1



# print_diamond(4)

### 5

def countdown():
    for i in range(10, 0, -1):
        print(i)
    print('Start!')

countdown()

### 6

def while_countdown():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print('Start!')

while_countdown()