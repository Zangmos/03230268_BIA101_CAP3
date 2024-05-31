file_path = '268.txt'

# Function to extract the first and last digits from a line
def extract_number_from_line(line):
    first_digit = None
    last_digit = None
    
    # Find the first digit
    for char in line:
        if char.isdigit():
            first_digit = char
            break
    
    # Find the last digit
    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break
    
    if first_digit and last_digit:
        return int(first_digit + last_digit)
    else:
        return 0

total_sum = 0

# Reading the file and processing each line
with open(file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()  # Remove any extra whitespace/newline characters
        number = extract_number_from_line(line)
        total_sum += number
        print(f'Line {line_number}: {line}, Number: {number}')

print(f'Total sum of all two-digit numbers: {total_sum}')

