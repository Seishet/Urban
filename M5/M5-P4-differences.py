class Building:
    total = 0
    def __init__(self):
        Building.total += 1

buildings = []

for i in range(0, 40):
    buildings.append(Building())

print(buildings[0].total)