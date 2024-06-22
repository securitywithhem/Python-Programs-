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