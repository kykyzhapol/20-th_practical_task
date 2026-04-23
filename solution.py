import random


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

    @classmethod
    def new_game(cls):
        """Очищает поле и случайным образом расставляет корабли."""
        # Очищаем поле
        cls.playing_field = [[0 for _ in range(10)] for _ in range(10)]

        # Список кораблей: (размер, количество)
        ships = [(4, 1), (3, 2), (2, 3), (1, 4)]

        # Функция проверки возможности размещения корабля
        def can_place(size, row, col, direction):
            # direction: 0 – горизонталь, 1 – вертикаль
            cells = []
            if direction == 0:  # горизонтально
                if col + size > 10:
                    return False
                for c in range(col, col + size):
                    cells.append((row, c))
            else:  # вертикально
                if row + size > 10:
                    return False
                for r in range(row, row + size):
                    cells.append((r, col))

            # Проверяем каждую клетку корабля и её соседей
            for r, c in cells:
                # Сама клетка должна быть 0
                if cls.playing_field[r][c] != 0:
                    return False
                # Проверяем всех соседей (включая диагонали)
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < 10 and 0 <= nc < 10:
                            if cls.playing_field[nr][nc] != 0:
                                return False
            return True

        # Размещаем корабли
        for size, count in ships:
            for _ in range(count):
                placed = False
                for attempt in range(1000):  # максимум попыток
                    row = random.randint(0, 9)
                    col = random.randint(0, 9)
                    direction = random.randint(0, 1)
                    if can_place(size, row, col, direction):
                        # Размещаем корабль
                        if direction == 0:
                            for c in range(col, col + size):
                                cls.playing_field[row][c] = 1
                        else:
                            for r in range(row, row + size):
                                cls.playing_field[r][col] = 1
                        placed = True
                        break
                if not placed:
                    raise RuntimeError("Не удалось расставить корабли, попробуйте снова.")

    def shot(self, x, y):
        """
        Выстрел по координатам (x, y), где x и y от 1 до 10.
        Выводит результат: 'попал', 'мимо', 'ошибка' или 'игровое поле не заполнено'.
        """
        # Проверяем, расставлены ли корабли (есть ли хотя бы одна 1)
        has_ships = any(1 in row for row in NavalBattle.playing_field)
        if not has_ships:
            print("игровое поле не заполнено")
            return

        # Преобразуем координаты в индексы (0..9)
        j, i = x - 1, y - 1
        if not (0 <= i < 10 and 0 <= j < 10):
            print("Координаты вне поля (допустимы 1..10)")
            return

        cell = NavalBattle.playing_field[i][j]

        # Проверяем, не стреляли ли уже в эту клетку
        if cell not in (0, 1):
            print("ошибка")
            return

        if cell == 1:
            print("попал")
            NavalBattle.playing_field[i][j] = self.player_symbol
        else:  # cell == 0
            print("мимо")
            NavalBattle.playing_field[i][j] = 'o'


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


import re

class RomanNumber:
    # Словарь для преобразования римских цифр в арабские
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def __init__(self, value):
        """
        Инициализация:
        - если value — строка с корректным римским числом, сохраняем в rom_value,
          int_value вычисляем через decimal_number()
        - если value — целое число от 1 до 3999, сохраняем в int_value,
          rom_value вычисляем через roman_number()
        - иначе выводим 'ошибка', соответствующий атрибут (rom_value или int_value) = None
        """
        if isinstance(value, str) and self.is_roman(value):
            self.rom_value = value.upper()
            self.int_value = self.decimal_number()  # вычисляем из римской строки
        elif isinstance(value, int) and self.is_int(value):
            self.int_value = value
            self.rom_value = self.roman_number()    # вычисляем римскую строку из числа
        else:
            print('ошибка')
            self.rom_value = None
            self.int_value = None

    def decimal_number(self):
        """
        Возвращает десятичный эквивалент:
        - если объект создан из римского числа, возвращает int
        - если создан из целого числа, возвращает это число
        - если ошибка, возвращает None
        """
        if hasattr(self, 'int_value') and self.int_value is not None:
            return self.int_value
        if hasattr(self, 'rom_value') and self.rom_value is not None:
            total = 0
            prev_value = 0
            for char in reversed(self.rom_value):
                current_value = self.roman_dict[char]
                if current_value < prev_value:
                    total -= current_value
                else:
                    total += current_value
                prev_value = current_value
            return total
        return None

    def roman_number(self):
        """
        Возвращает римскую строку:
        - если объект создан из целого числа, возвращает строку
        - если создан из римского числа, возвращает эту строку
        - если ошибка, возвращает None
        """
        if hasattr(self, 'rom_value') and self.rom_value is not None:
            return self.rom_value
        if hasattr(self, 'int_value') and self.int_value is not None:
            num = self.int_value
            if num < 1 or num > 3999:
                return None
            values = [
                (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
                (1, 'I')
            ]
            result = []
            for val, sym in values:
                while num >= val:
                    result.append(sym)
                    num -= val
            return ''.join(result)
        return None

    @staticmethod
    def is_int(value):
        """
        Статический метод. Возвращает True, если целое число value
        можно представить римским числом (1..3999), иначе False.
        """
        try:
            num = int(value)
        except (ValueError, TypeError):
            return False
        return 1 <= num <= 3999

    @staticmethod
    def is_roman(value):
        """
        Статический метод. Возвращает True, если строка value является
        корректным римским числом (1..3999), иначе False.
        """
        if not isinstance(value, str) or not value:
            return False
        pattern = r'^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        return bool(re.fullmatch(pattern, value.upper()))

    def __str__(self):
        """Строковое представление: возвращает rom_value или int_value в виде строки, иначе 'None'."""
        if self.rom_value is not None:
            return self.rom_value
        if self.int_value is not None:
            return str(self.int_value)
        return 'None'

    def __repr__(self):
        """Представление для разработчика."""
        if self.rom_value is not None:
            return self.rom_value
        if self.int_value is not None:
            return self.int_value
        return None