import unittest
from calculator import *

class TestMath(unittest.TestCase):
    def setUp(self):
        print("test start")

    # self.assertEqual(j.add_module(),16)   相等
    # self.assertNotEqual(j.add_module(),16) 不相等
    def test_add(self):
        j = Math(5,10)
        self.assertEqual(j.add(),15)

    def assertIn_test(self):
        self.assertIn("51zxw","51zxw,51ZXW")

    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMath("test_add"))
    suite.addTest(TestMath("assertIn_test"))

    runer = unittest.TextTestRunner()
    runer.run(suite)