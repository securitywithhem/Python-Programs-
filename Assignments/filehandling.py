def letter_frequency(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("File not founf. please provide a value")
        return
    
    frequency = {}


    for char in text:
        char = char.lower()
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    for letter, count in sorted(frequency.items()): 
        print(f"{letter}: {count}")

if __name__== "__main__":
    file_name = input("Enter the file name : ")
    letter_frequency(file_name)