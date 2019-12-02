class LetsIterate:
    def __init__(self, iterable_obj, return_odd_elements=True):
        self.iterable_obj = iterable_obj
        assert(isinstance(return_odd_elements, bool))
        if return_odd_elements:
            self.i = 1
        else:
            self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            res = self.iterable_obj[self.i]
        except IndexError:
            raise StopIteration
        self.i += 2
        return res
