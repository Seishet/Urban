class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

type_ = input('Введите тип первого строения: ')
floors_ = int(input('Введите количество этажей первого строения: '))
if floors_ < 1:
    print('Неправильное количество этажей')
else:
    building_1= Building(type_, floors_)

type_ = input('Введите тип второго строения: ')
floors_ = int(input('Введите количество этажей второго строения: '))
if floors_ < 1:
    print('Неправильное количество этажей')
else:
    building_2= Building(type_, floors_)

if building_1 == building_2:
    print('Строения идентичны')
else:
    print('Строения разные')