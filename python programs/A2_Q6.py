#QA
def least_frequent_char(n):
    char_freq = {}
    for char in n:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    min_freq = min(char_freq.values())
    least_freq_chars = [char for char, freq in char_freq.items() if freq == min_freq]
    return least_freq_chars


n = input("Enter the Text :   ")
print(least_frequent_char(n))  


#QB

for i in range(7):
    if i == 0 or i == 3 or i == 6:
        print(" ***** ")
    else:
        print("*     *" if i == 1 or i == 2 else "  *   ")