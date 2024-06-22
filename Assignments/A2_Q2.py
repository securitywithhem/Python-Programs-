def string_to_dict(n):
    dict_count = {}
    for char in n:
        if char in dict_count:
            dict_count[char] += 1
        else:
            dict_count[char] = 1
    return dict_count

n = str(input("Enter the String :  "))
print(string_to_dict(n))

