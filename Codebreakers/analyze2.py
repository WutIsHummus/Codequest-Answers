import sys
import string

# Define a function to calculate the frequency of each letter in a given string
def calculate_frequency(text):
    # Initialize an array of size 26 to represent the frequency count of each letter in the alphabet
    frequency = [0] * 26
    
    # Iterate through each character in the text
    for c in text:
        # If the character is a letter, increment the frequency count of the corresponding letter
        if c.isalpha():
            index = ord(c.upper()) - ord('A')
            frequency[index] += 1
    
    # Calculate the total number of letters in the text
    total = sum(frequency)
    
    # Calculate the relative frequency of each letter as a percentage
    result = []
    for i in range(26):
        letter = chr(i + ord('A'))
        freq = frequency[i] / total * 100 if total > 0 else 0
        result.append(f"{letter}: {freq:.2f}%")
    
    return result

# Read the number of test cases from input
num_cases = int(sys.stdin.readline())

# Iterate through each test case
for i in range(num_cases):
    # Read the number of lines of text to be provided
    num_lines = int(sys.stdin.readline())
    
    # Read the text to be analyzed
    text = ""
    for j in range(num_lines):
        text += sys.stdin.readline().strip()
    
    # Calculate the frequency of each letter in the text
    result = calculate_frequency(text)
    
    # Print the result
    print("\n".join(result))
