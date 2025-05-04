### 1

def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # [1, 2, 3, 4]

### 2

def generate_squares(n):
    return [x ** 2 for x in range(1, n + 1)]

print(generate_squares(5))

### 3

def merge_lists(list1: list, list2: list):
    return list(set(list1 + list2))

print(merge_lists([1, 2, 3], [3, 4, 5]))  # [1, 2, 3, 4, 5]

### 4

def is_sorted(lst: list):
    return lst == sorted(lst)

print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([1, 3, 2, 4, 5]))  # False

### 5

def merge_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists lengths are not equal')
    return [list1[x] + list2[x] for x in range(len(list1))]

print(merge_lists([1, 2, 3], [4, 5, 6]))  # [5, 7, 9]