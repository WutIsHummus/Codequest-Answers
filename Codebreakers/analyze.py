import sys
import string
from collections import Counter

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    lines = int(sys.stdin.readline().rstrip())
    letters = "" 
    #Get all the letters in one string
    for i in range(lines):
        line = (sys.stdin.readline().rstrip().translate(str.maketrans('', '', string.punctuation))).strip()
        letters += line
    #Remove spaces and make uppercase
    letters = letters.replace(" ", "").upper()
    #Count the letters
    count = Counter(letters)
    chars = len(letters)
    sorted_count = dict(sorted(count.items()))
    for key, value in sorted_count.items():
        print(f"{key}: {(value / chars) * 100:.2f}%")