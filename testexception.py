import unittest
from berryexception import BerryException

def raise_ex(key):
    raise BerryException(key)

class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, 1 == 1)

    def test(self):
        try:
            raise_ex(BerryException.keys.ONE)
        except BerryException as e:
            print(e)
            print(e.key)
            print(e.message)

            self.assertEqual('Error One', e.message)

    def test2(self):
        try:
            raise_ex('Generic message')
        except BerryException as e:
            print(e)
            print(e.key)
            print(e.message)
            self.assertEqual('Generic message', e.message)

if __name__ == '__main__':
    unittest.main()



