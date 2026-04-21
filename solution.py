class Circle:
    # Атрибуты класса
    pi = 3.1415
    all_circles = []  # список всех созданных экземпляров

    def __init__(self, radius=1):
        """Инициализация круга с заданным радиусом (по умолчанию 1)."""
        self.radius = radius
        # Добавляем текущий экземпляр в общий список
        Circle.all_circles.append(self)

    def area(self):
        """Возвращает площадь круга."""
        return Circle.pi * (self.radius ** 2)

    @staticmethod
    def total_area():
        """Возвращает суммарную площадь всех созданных кругов."""
        return sum(circle.area() for circle in Circle.all_circles)

    def __str__(self):
        return str(self.radius)

    def __repr__(self):
        return str(self.radius)


class NavalBattle:
    def __init__(self):
        pass

