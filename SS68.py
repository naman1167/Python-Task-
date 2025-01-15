def number_to_words():
    """Convert number to words."""
    
    # Dictionary for number words
    ones = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    
    teens = {
        '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen',
        '14': 'fourteen', '15': 'fifteen', '16': 'sixteen',
        '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'
    }
    
    tens = {
        '2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
        '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'
    }
    
    try:
        num = input("Enter a number: ")
        
        # Handle negative numbers
        if num.startswith('-'):
            print("negative", end=' ')
            num = num[1:]
            
        # Convert each digit to words
        if len(num) == 1:
            result = ones[num]
        elif len(num) == 2:
            if num[0] == '1':
                result = teens[num]
            else:
                result = tens[num[0]]
                if num[1] != '0':
                    result += '-' + ones[num[1]]
        else:
            # Handle digit by digit for larger numbers
            result = ' '.join(ones[digit] for digit in num)
        
        # Display results
        print(f"\nNumber: {num}")
        print(f"In words: {result}")
        
        # Additional information
        print(f"\nNumber of digits: {len(num)}")
        if num.isdigit():
            print(f"Sum of digits: {sum(int(d) for d in num)}")
            
    except KeyError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    number_to_words()
