from unittest import TestCase

from task1 import sum_of_squares_of_odd_numbers


class TestTaskOne(TestCase):

    def call_func_and_assert(self, input: list, expected: int):
        """
        Функция для вызова функции и проверки результата. Нужна, чтобы избежать дублирования кода.
        :param input: массив с целыми числами; входной аргумент тестируемой функции
        :param expected: ожидаемый результат
        :return: None
        """
        actual = sum_of_squares_of_odd_numbers(input)
        self.assertEqual(actual, expected, "Actual: %d, Expected: %d" % (actual, expected))

    def test_simple_input(self):
        input = [0, 1, 2, 3, 4]
        expected = 10
        self.call_func_and_assert(input, expected)

    def test_even_numbers(self):
        input = [2, 4, 6, 8]
        expected = 0
        self.call_func_and_assert(input, expected)

    def test_negative_numbers(self):
        input = [-1, -5, -7]
        expected = 75
        self.call_func_and_assert(input, expected)
