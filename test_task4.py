from unittest import TestCase
import threading

from dothreethings import Doer


class TestDoThreeThings(TestCase):
    @staticmethod
    def some_action_1():
        print("some action 1")

    @staticmethod
    def some_action_2():
        print("some action 2")

    @staticmethod
    def some_action_3():
        print("some action 3")

    def test_pipeline(self):
        d = Doer()
        t1 = threading.Thread(target=d.third, args=[self.some_action_3])
        t2 = threading.Thread(target=d.second, args=[self.some_action_2])
        t3 = threading.Thread(target=d.first, args=[self.some_action_1])

        for t in [t1, t2, t3]:  # type: threading.Thread
            t.start()
