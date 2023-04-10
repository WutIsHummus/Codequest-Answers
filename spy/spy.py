import sys
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    split = sys.stdin.readline().rstrip().split("|")
    firstPhrase = split[0].translate(str.maketrans('', '', string.punctuation))
    secondPhrase = split[1].translate(str.maketrans('', '', string.punctuation))
    valid = True
    for i in range(len(secondPhrase)):
        if secondPhrase[i].lower() not in firstPhrase.lower():
            valid = False
    if valid:
        print("That's my secret contact!")
    else:
        print("You're not a secret agent!")
