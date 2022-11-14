import unittest
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        print('this testis upper')
    def test_lower(self):
        self.assertEqual('FUN'.lower(),'fun')
        print('this test is lower')
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        print('this is upper')
    def test_islower(self):
        self.assertTrue('foo'.islower())
        print('this is lower')
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello','world'])
        with self.assertRaises(TypeError):
            s.split(2)
    if __name__ == '__main__':
        unittest.main()
