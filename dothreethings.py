from threading import Lock


class Doer:
    _first_lock = Lock()
    _first_lock.acquire()
    _second_lock = Lock()
    _second_lock.acquire()

    def first(self, action):
        # Следующую строчку не убирать
        action()
        self._first_lock.release()

    def second(self, action):
        while True:
            if not self._first_lock.locked():
                # Следующую строчку не убирать
                action()
                self._second_lock.release()
                break

    def third(self, action):
        while True:
            if not self._second_lock.locked():
                # Следующую строчку не убирать
                action()
                break
