def concatenate_strings(str_list):
    return ''.join(str_list)

def StrCount(str_list, str):
    count = 0
    for i in str_list:
        if i == str:
            count += 1
    return count

def find_first_non_repeating_char(str_list):
    char_count = {}
    for char in str_list:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

