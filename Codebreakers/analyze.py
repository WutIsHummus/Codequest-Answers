import sys
import string
from collections import Counter

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    lines = int(sys.stdin.readline().rstrip())
    letters = "" 
    for i in range(lines):
        line = (sys.stdin.readline().rstrip().translate(str.maketrans('', '', string.punctuation))).strip()
        letters += line
        print(letters)
    letters = letters.replace(" ", "").upper()
    count = Counter(letters)
    print(count)
    chars = len(letters)
    for key, value in count.items():
        print(f"{key}: {value / chars * 100:.2f}")