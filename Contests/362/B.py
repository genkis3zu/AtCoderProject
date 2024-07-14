import math

xA, yA = map(int, input().split())
xB, yB = map(int, input().split())
xC, yC = map(int, input().split())

AB = math.sqrt((xA - xB) ** 2 + (yA - yB) ** 2)
BC = math.sqrt((xB - xC) ** 2 + (yB - yC) ** 2)
CA = math.sqrt((xC - xA) ** 2 + (yC - yA) ** 2)

sides = sorted([AB, BC, CA])

a, b,c = sides[0], sides[1], sides[2]

if math.isclose(a**2 + b**2, c**2):
    print("Yes")
else:
    print("No")