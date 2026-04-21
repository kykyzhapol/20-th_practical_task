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
    # Атрибут класса: игровое поле 10x10, заполнено 0 (пусто)
    playing_field = [[0 for _ in range(10)] for _ in range(10)]

    def __init__(self, player_symbol):
        """Игрок получает свой символ (например, 'X' или 'A') для отметки попаданий."""
        self.player_symbol = player_symbol

    @staticmethod
    def show():
        """Статический метод: выводит текущее состояние поля на экран."""
        for row in NavalBattle.playing_field:
            line = []
            for cell in row:
                if cell == 0 or cell == 1:
                    # Клетка с кораблём (1) или пустая (0) – скрыта
                    line.append('~')
                elif cell == 'o':
                    line.append('o')
                else:
                    # Любой другой символ – это отметка попадания игрока
                    line.append(cell)
            print(' '.join(line))  # можно выводить без пробелов, но так нагляднее

    def shot(self, x, y):
        """
        Выстрел по координатам (x, y), где x и y от 1 до 10.
        Выводит "попал" или "мимо" и обновляет поле.
        """
        # Преобразуем координаты в индексы списка (0..9)
        j, i = x - 1, y - 1

        # Проверка границ (на случай некорректного ввода)
        if not (0 <= i < 10 and 0 <= j < 10):
            print("Координаты вне поля (1..10)")
            return

        cell = NavalBattle.playing_field[i][j]

        if cell == 1:
            # Попадание по кораблю
            print("попал")
            NavalBattle.playing_field[i][j] = self.player_symbol
        else:
            # Мимо: либо пусто (0), либо уже подбито/промах
            print("мимо")
            if cell == 0:
                NavalBattle.playing_field[i][j] = 'o'
            # Если клетка уже содержит символ игрока или 'o' – ничего не меняем



