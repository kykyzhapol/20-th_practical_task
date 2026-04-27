"""
Module containing several classes:

- Circle: represents circles with area calculation and total area tracking.
- NavalBattle: manages a simplified naval battle game (ship placement and shooting).
- RomanNumber: represents Roman numerals with arithmetic operations and conversions.
"""

import random
import re


class Circle:
    """Represents a circle with a given radius."""

    pi = 3.1415  # Approximate value of π
    all_circles = []  # List of all created circle instances

    def __init__(self, radius=1):
        """
        Initialize a circle with the specified radius.

        Args:
            radius: The radius of the circle (default 1).
        """
        self.radius = radius
        # Add the new instance to the class-level list
        Circle.all_circles.append(self)

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area (π * radius²).
        """
        return Circle.pi * (self.radius ** 2)

    @staticmethod
    def total_area():
        """
        Calculate the total area of all created circles.

        Returns:
            float: The sum of areas of all Circle instances.
        """
        return sum(circle.area() for circle in Circle.all_circles)

    def __str__(self):
        """Return the string representation of the circle's radius."""
        return str(self.radius)

    def __repr__(self):
        """Return the representation (same as __str__ for simplicity)."""
        return str(self.radius)


class NavalBattle:
    """Simplified naval battle game with ship placement and shooting."""

    # Class attribute: playing field 10x10, initially all zeros (empty)
    playing_field = [[0 for _ in range(10)] for _ in range(10)]

    def __init__(self, player_symbol):
        """
        Initialize a player with a symbol.

        Args:
            player_symbol: Character used to mark hits (e.g., 'X' or 'A').
        """
        self.player_symbol = player_symbol

    @classmethod
    def new_game(cls):
        """
        Clear the field and randomly place ships.

        Raises:
            RuntimeError: If ships cannot be placed after many attempts.
        """
        # Clear the field
        cls.playing_field = [[0 for _ in range(10)] for _ in range(10)]

        # Ship list: (size, count)
        ships = [(4, 1), (3, 2), (2, 3), (1, 4)]

        def can_place(size, row, col, direction):
            """
            Check if a ship can be placed at given position.

            Args:
                size: Length of the ship.
                row: Starting row index (0-9).
                col: Starting column index (0-9).
                direction: 0 = horizontal, 1 = vertical.

            Returns:
                bool: True if placement is valid, False otherwise.
            """
            cells = []
            if direction == 0:  # horizontal
                if col + size > 10:
                    return False
                for c in range(col, col + size):
                    cells.append((row, c))
            else:  # vertical
                if row + size > 10:
                    return False
                for r in range(row, row + size):
                    cells.append((r, col))

            # Check each cell of the ship and its neighbours
            for r, c in cells:
                # The cell itself must be empty (0)
                if cls.playing_field[r][c] != 0:
                    return False
                # Check all neighbours (including diagonals)
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < 10 and 0 <= nc < 10:
                            if cls.playing_field[nr][nc] != 0:
                                return False
            return True

        # Place ships
        for size, count in ships:
            for _ in range(count):
                placed = False
                for _ in range(1000):  # maximum attempts
                    row = random.randint(0, 9)
                    col = random.randint(0, 9)
                    direction = random.randint(0, 1)
                    if can_place(size, row, col, direction):
                        # Place the ship
                        if direction == 0:
                            for c in range(col, col + size):
                                cls.playing_field[row][c] = 1
                        else:
                            for r in range(row, row + size):
                                cls.playing_field[r][col] = 1
                        placed = True
                        break
                if not placed:
                    raise RuntimeError("Failed to place ships, try again.")

    def shot(self, x, y):
        """
        Perform a shot at coordinates (x, y), where x and y are from 1 to 10.

        Prints the result: 'попал' (hit), 'мимо' (miss), 'ошибка' (error),
        or 'игровое поле не заполнено' (field not initialised).

        Args:
            x: Column coordinate (1‑based).
            y: Row coordinate (1‑based).
        """
        # Check if ships are placed (any '1' exists)
        has_ships = any(1 in row for row in NavalBattle.playing_field)
        if not has_ships:
            print("игровое поле не заполнено")
            return

        # Convert to zero‑based indices
        j, i = x - 1, y - 1
        if not (0 <= i < 10 and 0 <= j < 10):
            print("Координаты вне поля (допустимы 1..10)")
            return

        cell = NavalBattle.playing_field[i][j]

        # Check if this cell has already been shot
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
        """
        Print the current state of the playing field.

        Ships (1) and empty cells (0) are shown as '~',
        misses as 'o', and hits as the player's symbol.
        """
        for row in NavalBattle.playing_field:
            line = []
            for cell in row:
                if cell == 0 or cell == 1:
                    # Hidden cell: ship or water
                    line.append('~')
                elif cell == 'o':
                    line.append('o')
                else:
                    # Player's symbol (hit)
                    line.append(cell)
            print(' '.join(line))


class RomanNumber:
    """
    Represents a Roman numeral (1‑3999) with conversion to/from integer.

    Supports arithmetic operations (+, -, *, /, //, %, **) with result
    automatically converted back to a Roman numeral if within 1‑3999,
    otherwise prints 'ошибка' and returns an error object.
    """

    # Mapping of Roman symbols to integer values
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
        Initialise a RomanNumber.

        Args:
            value: Either a string (Roman numeral), an integer (1‑3999), or None.
                   If the value is invalid, prints 'ошибка' and sets both
                   internal attributes to None.
        """
        if value is None:
            self.rom_value = None
            self.int_value = None
        elif isinstance(value, str) and self.is_roman(value):
            self.rom_value = value.upper()
            self.int_value = self._to_int()
        elif isinstance(value, int) and self.is_int(value):
            self.int_value = value
            self.rom_value = self._to_roman()
        else:
            print('ошибка')
            self.rom_value = None
            self.int_value = None

    def _to_int(self):
        """
        Convert the internal Roman string to an integer.

        Returns:
            int or None: The integer value, or None if no Roman value.
        """
        if self.rom_value is None:
            return None
        total = 0
        prev = 0
        for ch in reversed(self.rom_value):
            cur = self.roman_dict[ch]
            if cur < prev:
                total -= cur
            else:
                total += cur
            prev = cur
        return total

    def _to_roman(self):
        """
        Convert the internal integer to a Roman string.

        Returns:
            str or None: The Roman numeral, or None if no integer value.
        """
        if self.int_value is None:
            return None
        num = self.int_value
        # Value-symbol pairs in descending order
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

    def decimal_number(self):
        """
        Return the decimal integer equivalent.

        Returns:
            int or None: The integer value, or None if the object is invalid.
        """
        return self.int_value

    def roman_number(self):
        """
        Return the Roman numeral string.

        Returns:
            str or None: The Roman string, or None if the object is invalid.
        """
        return self.rom_value

    @staticmethod
    def is_int(value):
        """
        Check if the value is a valid integer in the range 1‑3999.

        Args:
            value: Any value.

        Returns:
            bool: True if value can be converted to an int and is between 1 and 3999.
        """
        try:
            num = int(value)
        except (ValueError, TypeError):
            return False
        return 1 <= num <= 3999

    @staticmethod
    def is_roman(value):
        """
        Check if the string is a valid Roman numeral (1‑3999).

        Args:
            value: A string.

        Returns:
            bool: True if the string matches the Roman numeral pattern.
        """
        if not isinstance(value, str) or not value:
            return False
        pattern = r'^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        return bool(re.fullmatch(pattern, value.upper()))

    @staticmethod
    def _error_instance():
        """
        Create an error instance (both attributes None).

        Returns:
            RomanNumber: An object with rom_value = None and int_value = None.
        """
        err = RomanNumber.__new__(RomanNumber)
        err.rom_value = None
        err.int_value = None
        return err

    # ---------- Arithmetic operators ----------

    def _check_operand(self, other):
        """
        Prepare operands for arithmetic operation.

        Args:
            other: The second operand (may be int, str, or RomanNumber).

        Returns:
            tuple: (self_int, other_int) or (None, None) if either operand is invalid.
        """
        if self.int_value is None:
            return None, None
        # Try to convert other to RomanNumber if it's not already one
        if not isinstance(other, RomanNumber):
            try:
                other = RomanNumber(other)
            except Exception:
                return None, None
        if other.int_value is None:
            return None, None
        return self.int_value, other.int_value

    def _make_result(self, result_int):
        """
        Create a new RomanNumber from an integer result.

        If the result is within 1‑3999, returns a valid RomanNumber.
        Otherwise prints 'ошибка' and returns an error instance.

        Args:
            result_int: The integer result of an operation.

        Returns:
            RomanNumber: Valid result or error instance.
        """
        if result_int is not None and 1 <= result_int <= 3999:
            return RomanNumber(result_int)
        print('ошибка')
        return RomanNumber._error_instance()

    def __pow__(self, other):
        a, b = self._check_operand(other)
        if a is None or b is None:
            print('ошибка')
            return RomanNumber._error_instance()
        result = a ** b
        return self._make_result(result)

    def __rpow__(self, other):
        # other ** self
        tmp = RomanNumber(other) if not isinstance(other, RomanNumber) else other
        return tmp ** self

    def __add__(self, other):
        a, b = self._check_operand(other)
        if a is None or b is None:
            print('ошибка')
            return RomanNumber._error_instance()
        return self._make_result(a + b)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        a, b = self._check_operand(other)
        if a is None or b is None:
            print('ошибка')
            return RomanNumber._error_instance()
        return self._make_result(a - b)

    def __rsub__(self, other):
        # other - self
        tmp = RomanNumber(other) if not isinstance(other, RomanNumber) else other
        return tmp - self

    def __mul__(self, other):
        a, b = self._check_operand(other)
        if a is None or b is None:
            print('ошибка')
            return RomanNumber._error_instance()
        return self._make_result(a * b)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        a, b = self._check_operand(other)
        if a is None or b is None or b == 0:
            print('ошибка')
            return RomanNumber._error_instance()
        # Only integer division allowed (must be exact)
        if a % b != 0:
            print('ошибка')
            return RomanNumber._error_instance()
        return self._make_result(a // b)

    def __rtruediv__(self, other):
        # other / self
        tmp = RomanNumber(other) if not isinstance(other, RomanNumber) else other
        return tmp / self

    def __floordiv__(self, other):
        a, b = self._check_operand(other)
        if a is None or b is None or b == 0:
            print('ошибка')
            return RomanNumber._error_instance()
        return self._make_result(a // b)

    def __rfloordiv__(self, other):
        tmp = RomanNumber(other) if not isinstance(other, RomanNumber) else other
        return tmp // self

    def __mod__(self, other):
        a, b = self._check_operand(other)
        if a is None or b is None or b == 0:
            print('ошибка')
            return RomanNumber._error_instance()
        return self._make_result(a % b)

    def __rmod__(self, other):
        tmp = RomanNumber(other) if not isinstance(other, RomanNumber) else other
        return tmp % self

    # ---------- String representation ----------
    def __str__(self):
        """Return the Roman string or the integer as string if available, else 'None'."""
        if self.rom_value is not None:
            return self.rom_value
        if self.int_value is not None:
            return str(self.int_value)
        return 'None'

    def __repr__(self):
        """Return the representation (Roman string or integer, or None)."""
        if self.rom_value is not None:
            return self.rom_value
        if self.int_value is not None:
            return str(self.int_value)
        return None
