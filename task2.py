import time


def func_timeit_decorator(func):
    def wrapper_func(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
    return wrapper_func


class ClassTimeitDecorator:

    def __init__(self, func):
        self.function = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        self.function(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
