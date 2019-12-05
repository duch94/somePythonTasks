import time


def func_timeit_decorator(func):
    """
    Функция-декоратор для подсчета времени работы оборачиваемой функции.
    :param func: оборачиваемая функция
    :return: обёрнутая функция
    """

    def wrapper_func(*args, **kwargs):
        """
        Функция, реализующая подсчет времени работы оборачиваемой функции, вызываемой с помощью замыкания.
        :param args: передаваемые в оборачиваемую функцию позиционные аргументы
        :param kwargs: передаваемые в оборачиваемую функцию именованные аргументы
        :return: None
        """
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)

    return wrapper_func


class ClassTimeitDecorator:
    """
    Класс-декоратор для подсчета времени работы оборачиваемой функции
    """

    def __init__(self, func):
        """
        Метод-конструктор класса, который принимает в себя оборачиваемую функцию.
        :param func: оборачиваемая функция
        :return: self
        """
        self.function = func

    def __call__(self, *args, **kwargs):
        """
        Магический метод, фактически перегружающий оператор (). Реализует подсчет времени работы оборачиваемой функции.
        :param args: передаваемые в оборачиваемую функцию позиционные аргументы
        :param kwargs: передаваемые в оборачиваемую функцию именованные аргументы
        :return: None
        """
        start_time = time.time()
        self.function(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
