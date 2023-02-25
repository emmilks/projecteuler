import unittest


def euler01(n):
    return sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)


class TestEuler01(unittest.TestCase):
    def test_euler01(self):
        self.assertEqual(euler01(10), 23)
        self.assertEqual(euler01(1000), 233168)
