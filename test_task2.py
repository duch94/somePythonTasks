from unittest import TestCase
from time import sleep, time

from task2 import func_timeit_decorator, ClassTimeitDecorator


class TestDecorators(TestCase):

    def test_func_decorator(self):
        @func_timeit_decorator
        def some_func():
            sleep(2)

        start_time = time()
        some_func()
        end_time = time()
        self.assertGreater(end_time - start_time, 2.0)

    def test_class_decorator(self):
        @ClassTimeitDecorator
        def some_func():
            sleep(2)

        start_time = time()
        some_func()
        end_time = time()
        self.assertGreater(end_time - start_time, 2.0)
