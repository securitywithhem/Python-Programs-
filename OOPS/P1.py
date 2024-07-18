def number_to_words(number):
    digit_to_word = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    words = [digit_to_word[digit] for digit in str(number)]
    return ' '.join(words)

User = input("Enter the Number:  ")
print("The Number in word format is ",number_to_words(User))