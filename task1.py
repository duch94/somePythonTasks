def sum_of_squares_of_odd_numbers(array: list):
    """
    Функция, принимающая в качестве параметра список (list) целых чисел и возвращающую сумму квадратов всех
    нечетных чисел в данном списке.
    :param array: список целых чисел
    :return: сумма квадратов всех четных чисел
    """
    return sum([x*x if x % 2 == 1 else 0 for x in array])

