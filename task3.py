class LetsIterate:
    """
    Класс, реализующий итератор передаваемого объекта
    """
    def __init__(self, iterable_obj, return_odd_elements=True):
        """
        Конструктор, в который передается итерируемый объект и
        флаг для указания какие по четности элементы использовать.
        :param iterable_obj: итерируемый объект
        :param return_odd_elements: True, если нужно возвращать нечетные элементы
        """
        self.iterable_obj = iterable_obj
        assert(isinstance(return_odd_elements, bool))
        if return_odd_elements:
            self.i = 1
        else:
            self.i = 0

    def __iter__(self):
        """
        Магический метод, необходимый для того, чтобы класс считался итератором.
        :return: self
        """
        return self

    def __next__(self):
        """
        Магический метод, возвращающий следующий четный или нечетный элемент итерируемого объекта.
        :return: следующий четный или нечетный элемент итерируемого объекта
        """
        try:
            res = self.iterable_obj[self.i]
        except IndexError:
            raise StopIteration
        self.i += 2
        return res
