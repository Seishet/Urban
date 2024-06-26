class House:
    def __init__(self):
        self.number_of_floors = 0

    def setNewNumberOfFloors(self, floors):
        self.number_of_floors = floors
        if floors % 10 == 1:
            print(f'Объект класса дом создан. Задан {self.number_of_floors} этаж')
        elif floors % 10 < 5:
            print(f'Объект класса дом создан. Задано {self.number_of_floors} этажа')
        else:
            print(f'Объект класса дом создан. Задано {self.number_of_floors} этажей')


house = House()
floors_ = int(input('Введите количество этажей: '))
if floors_ < 1:
    print('Неправильное количество этажей')
else:
    house.setNewNumberOfFloors(floors_)