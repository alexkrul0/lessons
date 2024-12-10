import math


class Figure:
    sides_count = 0
    __sides = []

    def __init__(self, __color, *args, filled=True):
        self.__color = __color
        self.filled = filled
        if self.__is_valid_sides(*args):
            for i in range(0, self.sides_count):
                self.__sides.append(*args)
        else:
            for i in range(0, self.sides_count):
                self.__sides.append(1)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (isinstance(r, int) and 0 <= r <= 255 and
                isinstance(g, int) and 0 <= g <= 255 and
                isinstance(b, int) and 0 <= b <= 255):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *args):
        side_1 = True
        side_2 = True
        count = 0
        for i in args:
            if i == float or i <= 0:
                side_1 = False
                break
        for j in args:
            count += 1
        if count != self.sides_count and count != 1:
            side_2 = False
        if side_1 and side_2:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        count = 0
        for i in new_sides:
            count += 1
        if count == self.sides_count:
            self.__sides = []
            for j in range(0, len(self.__sides) + 1):
                self.__sides.append(*new_sides)
        else:
            return self.__sides

    def clean_side(self):
        self.__sides = []


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, __sides, filled=True):
        super().__init__(__color, __sides, filled=True)
        self.__radius = __sides / 2 * math.pi

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = sum(self.set_sides()) / 2
        s = math.sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))
        return s


class Cube(Figure):
    sides_count = 12

    # __sides = []

    def __init__(self, color, *args):
        self.clean_side()
        super().__init__(color, *args)
        self.__sides = self.get_sides()

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# circle1.get_square()
# print(cube1.get_volume())

# Проверка на изменение цветов
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра круга
print(len(circle1))

# Проверка объема куба
print(cube1.get_volume())
