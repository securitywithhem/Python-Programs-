#Qa
import collections

# Define a dictionary to map words to digits
word_to_digit = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
}

# Define a list of words
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']

# Convert each word to its corresponding digit
digits = [word_to_digit[word] for word in words]

# Find the frequency of each digit
frequency = collections.Counter(digits)

# Print the frequency of each digit
for digit, count in frequency.items():
    print(f"Digit {digit}: {count}")




#Qb

def draw_horizontal_histogram(values):
    max_value = max(values)
    for value in values:
        print("*" * value + " " * (max_value - value))

def draw_vertical_histogram(values):
    max_value = max(values)
    for i in range(max_value, 0, -1):
        for value in values:
            if value >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Example usage
values = [3, 5, 2, 7, 1, 4]

print("Horizontal Histogram:")
draw_horizontal_histogram(values)

print("Vertical Histogram:")
draw_vertical_histogram(values)