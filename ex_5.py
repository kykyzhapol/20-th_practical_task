'''
Доработайте Задание 4.  Экземпляр класса может инициализироваться как строкой - записью римского числа,
так и десятичным целым числом. Запись десятичного числа должна храниться в атрибуте int_value. В случае,
если этим числом представить римское число невозможно, то на экран должно выводиться сообщение 'ошибка' и
атрибут int_value должен иметь значение None. Метод roman_number() должен возвращать строку - эквивалент
этого числа в римской системе счисления. Опишите статический метод is_int(value),
который возвращает True - если целое число value представимо римским, и False - в противном случае.
'''


from solution import RomanNumber

num_1 = RomanNumber(214)
print(num_1.int_value)
print(num_1.roman_number())
print(num_1.rom_value)
print(num_1)
num_2 = RomanNumber(5690)
print(num_2.int_value)
num_3 = RomanNumber('DXCVII')
print(num_3.int_value)
print(num_3.rom_value)
print(num_3)
print(RomanNumber.is_int(-614))
print(RomanNumber.is_int(3758))
