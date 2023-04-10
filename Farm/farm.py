import sys
cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    turkeys, goats, horses = (sys.stdin.readline().rstrip()).split(' ')
    turkeyLegs = int(turkeys) * 2
    goatLegs = int(goats) * 4
    horseLegs = int(horses) * 4
    print(turkeyLegs + goatLegs + horseLegs)
   
