### 1

def char_frequency(s: str):
    result = dict()
    for char in s:
        result.update({char: s.count(char)})
    return result

print(char_frequency("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

### 2

def merge_dicts(dic1: dict, dic2: dict):
    for value in dic2.items():
        key, val = value
        if key in dic1.keys():
            dic1.update({key: dic1[key] + val})
        else:
            dic1.update({key: val})
    return dic1

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dicts(dict1, dict2))  # {"a": 1, "b": 5, "c": 4}

### 3

def dict_to_lists(my_dict: dict):
    return tuple(([x for x in my_dict.keys()], [x for x in my_dict.values()]))

my_dic = {"a": 1, "b": 2, "c": 3}
print(dict_to_lists(my_dic))  # (["a", "b", "c"], [1, 2, 3])


### 4

def group_by_first_letter(strings: list):
    first_letters_list = sorted(list(set(word[0] for word in strings)))
    result = {}
    for char in first_letters_list:
        values = [word for word in strings if word[0] == char]
        result.update({char: values})
    return result

strings_1 = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings_1))
# {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}


### 5

def extract_subdict(my_dict, keys):
    result = {}
    for key in my_dict.keys():
        if key in keys:
            result.update({key: my_dict[key]})
    return result

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = ["a", "c"]
print(extract_subdict(my_dict, keys))  # {"a": 1, "c": 3}