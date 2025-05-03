roflo_list = [1, 5, 7, 4, 2, 7]

# i = 0
# while i < len(roflo_list) - 1:
#     a = roflo_list[i]
#     b = roflo_list[i+1]
#     if a > b:
#         roflo_list[i] = b
#         roflo_list[i+1] = a
#         i = 0
#     i += 1

was_changed = True
while was_changed:
    i = 0
    was_changed = False
    while i + 1 < len(roflo_list):
        a = roflo_list[i]
        b = roflo_list[i+1]
        if a > b:
            roflo_list[i] = b
            roflo_list[i+1] = a
            was_changed = True
        i += 1


print(roflo_list)