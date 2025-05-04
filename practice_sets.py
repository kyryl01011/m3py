### 1

import string


def get_unique_elements(lst):
    return list(set(lst))

print(get_unique_elements([1, 2, 2, 3, 4, 4, 4, 5]))  # [1, 2, 3, 4, 5]

### 2

def is_unique_list(lst):
    return len(lst) == len(set(lst))

print(is_unique_list([1, 2, 3, 4]))  # True
print(is_unique_list([1, 2, 2, 3]))  # False

### 3

def get_unique_vowels(s):
    return set([vowel for vowel in ''.join([char for char in s if char not in string.punctuation]).lower() if vowel in ['a', 'e', 'i', 'o', 'u']])

print(get_unique_vowels("Hello World"))  # {'e', 'o'}