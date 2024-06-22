def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    
    def one(num):
        return ones[num]

    def two_less_20(num):
        if num < 10:
            return one(num)
        elif 10 < num < 20:
            return teens[num - 11]
        return tens[num // 10] + ('' if num % 10 == 0 else ' ' + one(num % 10))

    def two(num):
        if num < 10:
            return one(num)
        elif num < 20:
            return two_less_20(num)
        else:
            return tens[num // 10] + ('' if num % 10 == 0 else ' ' + one(num % 10))

    def three(num):
        hundred = num // 100
        rest = num % 100
        if hundred == 0:
            return two(rest)
        else:
            if rest == 0:
                return one(hundred) + ' hundred'
            else:
                return one(hundred) + ' hundred and ' + two(rest)

    def convert_number(num):
        if num == 0:
            return 'zero'
        elif num < 100:
            return two(num)
        elif num < 1000:
            return three(num)

    return convert_number(n)

def amount_to_words(amount):
    integral, decimal = str(amount).split('.')
    integral = int(integral)
    decimal = int(decimal) if decimal else 0
    
    integral_words = number_to_words(integral)
    decimal_words = ' '.join([number_to_words(int(d)) for d in decimal])
    
    return integral_words + ' point ' + decimal_words if decimal else integral_words

def digit_to_word(amount):
    digits = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    amount_str = str(amount)
    return ' '.join(digits[d] for d in amount_str)

def main():
    amount = input("Enter an amount with at least one integral digit and zero or two decimal digits: ")
    try:
        amount = float(amount)
        if not (amount % 1 == 0 or (len(str(amount).split('.')[1]) in [0, 2])):
            raise ValueError("Amount must have zero or two decimal digits.")
        
        print("Each digit in words:", digit_to_word(amount))
        print("Amount in words:", amount_to_words(amount))
    except ValueError as e:
        print("Invalid input:", e)

if __name__ == "__main__":
    main()
