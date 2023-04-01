'''
В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot.
Чем больше тестов на каждую функцию - тем лучше
'''

#________________________________________________________________________
# 1. filter function
# фильтруем чётные в диапазоне от 1 до 10

# # с использованием отдельной функции
# def filter_even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
#
# def even_result():
#     return filter(filter_even, range(1, 11))

# с использованием lambda
def even_result():
    return list(filter(lambda x: (x % 2 == 0), range(1, 11)))


# even_filtered = even_result()

# print(even_filtered)

# for x in even_filtered:
#     print(x)


def test_filter_even():
    assert even_result() == [2, 4, 6, 8, 10]


# 2. map function
# возводим в квадрат числа из диапозона от 1 до 5 и выводим в формате списка
def square_result():
    return list(map(lambda x: (x ** 2), range(1, 6)))


def test_square_result():
    assert square_result() == [1, 4, 9, 16, 25]

#3. sorted function
# сортируем диапазон от 1 до 5 в обратном порядке
def sorted_result():
    return list(sorted(range(1, 6), reverse=True))


def test_sorted_result():
    assert sorted_result() == [5, 4, 3, 2, 1]


#________________________________________________________________________
import math

#4. pi function
def test_pi():
    assert math.pi == 3.141592653589793

#5. sqrt function
def test_sqrt():
    assert math.sqrt(4) == 2
    assert math.sqrt(9) == 3
    assert math.sqrt(16) == 4
    assert math.sqrt(25) == 5

#6. pow function
def test_pow():
    assert math.pow(2, 2) == 4
    assert math.pow(3, 2) == 9
    assert math.pow(4, 2) == 16
    assert math.pow(5, 2) == 25
    assert math.pow(2, 3) == 8
    assert math.pow(4, 3) == 64

#7. hypot function
def test_hypot():
    assert math.hypot(3, 4) == 5

print(math.hypot(3, 4))
