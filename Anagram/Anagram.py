import sys

def is_anagram(str1, str2):
    if str1 ==str2:
        return False
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)
    
    return str1_sorted == str2_sorted

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    a, b = (sys.stdin.readline().rstrip()).split('|')
    if is_anagram(a, b):
        print(f'{a}|{b} = ANAGRAM')
    else:
        print(f'{a}|{b} = NOT AN ANAGRAM')

