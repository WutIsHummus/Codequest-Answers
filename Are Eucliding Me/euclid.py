import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    a, b = map(int, sys.stdin.readline().rstrip().split(","))
    g = gcd(a, b)
    minued, subtrahend = max(a,b), min(a,b)
    while minued - subtrahend != 0:
        dif = minued - subtrahend
        print(f"{minued}-{subtrahend}={dif}")
        minued, subtrahend = max(dif, subtrahend), min(dif, subtrahend)
    print(f"{minued}-{subtrahend}={minued - subtrahend}")
    if g == 1:
        print("COPRIME")
    else:
        print("NOT COPRIME")
