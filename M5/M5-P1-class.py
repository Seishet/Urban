class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        new_floor = int(new_floor)
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor+1):
                print('Этаж: ', i)

house = House('ЖК Эльбрус', 30)
new_floor = input('Введите этаж: ')
house.go_to(new_floor)