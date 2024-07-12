
from projekt import S
import unittest as ut

class TestS(ut.TestCase):
    def test_rounded(self):
        result = round(S(2, 5), 15)
        self.assertEqual(result, 2e-15)

    def test_negative_value(self):
        result = round(S(2, -5), 2)
        self.assertEqual(result, -1290.47)

if __name__ == "__main__":
    ut.main()