from ambidand import dand, dor, dxor, dif, dconst
import unittest

miscellany = [0, 1, -1, [], True, False]

class TestAll(unittest.TestCase):
    def assertCallable(self, thing):
        self.assertTrue(callable(thing))


    def test_dand(self):
        self.assertCallable(dand)
        for item in miscellany:
            self.assertCallable(dand(item))

        self.assertTrue(dand(True)(True))
        self.assertFalse(dand(False)(True))
        self.assertFalse(dand(True)(False))
        for item in miscellany:
            self.assertFalse(dand(False)(item))


    def test_dor(self):
        self.assertCallable(dor)
        for item in miscellany:
            self.assertCallable(dor(item))

        self.assertTrue(dor(True)(True))
        self.assertTrue(dor(False)(True))
        for item in miscellany:
            self.assertTrue(dor(True)(item))
        self.assertFalse(dor(False)(0))


    def test_dxor(self):
        self.assertCallable(dxor)
        for item in miscellany:
            self.assertCallable(dxor(item))

        self.assertTrue(dxor(True)(False))
        self.assertTrue(dxor(False)(True))
        self.assertFalse(dxor(False)(False))
        self.assertFalse(dxor(True)(True))


    def test_dconst(self):
        self.assertCallable(dconst)
        for item in miscellany:
            self.assertCallable(dconst(item))

            for other_item in miscellany:
                self.assertEqual(item, dconst(item)(other_item))


    def test_dif(self):
        self.assertCallable(dif)
        for item in miscellany:
            self.assertCallable(dif(item))

        self.assertEqual(1, dif(True)(1,2))
        self.assertEqual(2, dif(False)(1,2))


if __name__ == "__main__":
    unittest.main()
