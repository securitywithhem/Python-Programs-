letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)
def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        index = letters.find(letter)
        new_index = index + key
        if new_index >= num_letters:
            new_index -= num_letters
        ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        index = letters.find(letter)
        new_index = index - key
        if new_index < 0 :
            new_index += num_letters
        plaintext += letters[new_index]
    return plaintext


print()
print('*** CAESER CIPHER PROGRAM ***')
print()

print("Do you want to encrypt or decrypt it ??")
user_input = input ('e/d: ').lower()
print()

if user_input == 'e':
    print("ENCRYPTION MODE ONN")
    print()
    plaintext = input("Enter the Text : ")
    key = int(input("Enter the key (Between 1 to 26 ):"))
    ciphertext = encrypt(plaintext,key)
    print(f'CIPHERTEXT: {ciphertext}')

else: 

    print("DECRYPTION MODE ONN")
    print()
    ciphertext = input("Enter the Text : ")
    key = int(input("Enter the key (Between 1 to 26 ):"))
    plaintext = decrypt(ciphertext,key)
    print(f'CIPHERTEXT: {plaintext}')



# from typing import Counter

# string_input = input("Enter a string: ").lower()
# list = list(string_input)
# print(list)

# shifted_chars = []
# for char in list:
#     if char == ' ':
#         shifted_chars.append(' ')
#     else:
#         unicode_value = ord(char)
#         shifted_unicode = ((unicode_value + 3) - 26) if unicode_value + 3 > 122 else unicode_value + 3
#         shifted_char = chr(shifted_unicode)
#         shifted_chars.append(shifted_char)

# print(shifted_chars)

# shifted_string = ''.join(shifted_chars)
# print(shifted_string)

# frequency = Counter(shifted_string)
# print(frequency)

# frequency_dict = dict(frequency)
# print(frequency_dict)

# sorted_dict = dict(sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True))
# print(sorted_dict)

# keys_list = []
# for key in sorted_dict.keys():
#     keys_list.append(key)
# print(keys_list)

# Letter_frequencies = ['e','t','a','o','i','n','s','r','h','d','l','u','c','m','f','y','w','g','p','b','v','k','x','q','j','z']

# keys_list = [key for key in sorted_dict.keys() if key != ' ']
# print(keys_list)

# first_key = keys_list[0]
# first_frequency = Letter_frequencies[0]


# for i in range(1, len(keys_list)):
#     current_key = keys_list[i]
#     current_frequency = Letter_frequencies[i]
#     difference = ord(current_key) - ord(current_frequency)
#     print(abs(difference))
    
#     unshifted_chars = []
#     for char in shifted_chars:
#         if char == ' ':
#             unshifted_chars.append(' ')
#         else:
#             unicode_value = ord(char)
#             reversed_unicode = ((unicode_value - abs(difference)) + 26) if unicode_value - abs(difference) < 97 else unicode_value - abs(difference);
#             reversed_char = chr(reversed_unicode)
#             unshifted_chars.append(reversed_char)

#     reversed_string = ''.join(unshifted_chars)
#     print(reversed_string)

#     user_input = input("Continue to the next frequency? (yes/no): ")
#     if user_input.lower() == "no":
#         break



