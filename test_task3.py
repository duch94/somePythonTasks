from unittest import TestCase

from task3 import LetsIterate


class TestMyIterator(TestCase):

    def call_iterator_and_assert(self, some_list, return_odd_elements, expected):
        actual = []
        iterator = LetsIterate(iterable_obj=some_list, return_odd_elements=return_odd_elements)
        for i in iterator:
            actual.append(i)
        self.assertEqual(expected, actual)

    def test_odd_elements(self):
        some_list = [0, 10, 20, 30, 40, 50]
        expected = [10, 30, 50]
        self.call_iterator_and_assert(some_list=some_list, return_odd_elements=True, expected=expected)

    def test_even_elements(self):
        some_list = [0, 10, 20, 30, 40, 50]
        expected = [0, 20, 40]
        self.call_iterator_and_assert(some_list=some_list, return_odd_elements=False, expected=expected)
