from time import sleep


class Doer:
    _first_executed = False
    _second_executed = False

    def first(self, action):
        # Следующую строчку не убирать
        action()
        self._first_executed = True

    def second(self, action):
        while not self._first_executed:
            sleep(0.1)
        # Следующую строчку не убирать
        action()
        self._second_executed = True

    def third(self, action):
        while not self._second_executed:
            sleep(0.1)
        # Следующую строчку не убирать
        action()
