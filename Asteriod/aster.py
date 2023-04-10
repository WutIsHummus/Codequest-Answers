import sys
import math

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    asteroidList = []
    asteroidNum = int(sys.stdin.readline().rstrip())
    for i in range(asteroidNum):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        hypotenuse = math.hypot(x, y)
        asteroidList.append((f"{x} {y}", hypotenuse))
    asteroidList = sorted(asteroidList, key=lambda x: x[1])
    for asteroid in asteroidList:
        print(f"{asteroid[0]}")
