### 1

rectangle_data = dict(height=3, width=5)

def rectangle_area(height, width):
    return height * width

print(f'Rectangle area with width {rectangle_data['width']} and height {rectangle_data['height']} equals {rectangle_area(rectangle_data['height'], rectangle_data['width'])}')

### 2

timer = 3672

def convert_seconds(secs):
    hours = int(secs / 3600)
    if (secs - hours * 3600) % 60 == 0:
        minutes = int((secs - hours * 3600) / 60)
    else:
        minutes = int((secs - hours * 3600) / 60) + 1
    return hours, minutes

timer_hours, timer_minutes = convert_seconds(timer)

print(f'In {timer} seconds {timer_hours} hour(s) and {timer_minutes} minut(es)')

### 3

def power_of(number, exponent = 2):
    return number ** exponent

first_test = [3, 4]
second_test = [5]
print(f'Number {first_test[0]} with exponent {first_test[1]} is {power_of(first_test[0], first_test[1])}')
print(f'Quarter of {second_test[0]} is {power_of(second_test[0])}')

### 4

def count_items(*args):
    return len([*args])

print(f'Args given: {count_items(1, 2, 3, 4, 5)}')