class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args)
        return super().__new__(cls)

    def __init__(self, name, number_of_Floors):
        self.name = name
        self.number_of_floors = number_of_Floors

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        text = f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
        return text

    def __del__(self):
        text = f'{self.name} снесен, но он останется в истории'
        print(text)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрешки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)
