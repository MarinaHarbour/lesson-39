import math
class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=False):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            return (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255)
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Некорректные значения цвета. Цвет останется прежним.")

    def __is_valid_sides(self, *sides):
        if len(sides) != len(self.__sides):
            return False
        for side in sides:
            if not (isinstance(side, int) and side > 0):
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print("Некорректные значения сторон. Стороны останутся прежними.")


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        return int(self.get_sides()[0])**2 / (4 * math.pi)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, a, b, c, color, *sides):
        self.a = a
        self.b = b
        self.c = c
        super().__init__(color, *sides)

    def get_square(self):
        p = 0.5 * (self.a+self.b+self.c)
        return math.sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))




class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = sides * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        return int(self.get_sides()[0]) ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle(10, 15, 10, (200,200,200), 3)



# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка площади (круга)
print(circle1.get_square())

# Проверка площади (треугольника)
print(triangle1.get_square())
