### 1
import string
from operator import indexOf


def is_anagram(s1: str, s2: str):
    for char in s2:
        if char.lower() not in s1.lower() or len(s1) != len(s2):
            return False
    return True

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False

### 2

def is_palindrome(s: str):
    pure_string = s.replace(',', '').replace('.', '').replace(' ', '').replace(':', '').lower()
    if pure_string == pure_string[::-1]:
        return True
    else:
        return False

print(is_palindrome("A man, a plan, a canal: Panama"))  # True

print(is_palindrome("racecar"))                         # True

print(is_palindrome("hello"))                           # False

### 3

def longest_word(s: str):
    longest = ''
    for word in ''.join(char for char in s if char not in string.punctuation).lower().split(' '):
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word("In the middle of a vast desert, an extraordinary adventure awaits"))

### 4

def format_phone_number(digits):
    return f'({digits[:3]}) {digits[3:6]}-{digits[6:]}'

print(format_phone_number("1234567890"))  # "(123) 456-7890”

### 5

def remove_duplicates(s: str):
    result = ''
    for char in s:
        if char not in result:
            result += char
    return result

print(remove_duplicates("programming"))  # "progamin”

### 6

def is_unique(s):
    result = ''
    for char in s:
        if char not in result:
            result += char
    return len(result) == len(s)

print(is_unique("abcdef"))  # True
print(is_unique("hello"))  # False