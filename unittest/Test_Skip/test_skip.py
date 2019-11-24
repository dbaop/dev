from calculator import *
from test_add import *
import unittest
# unittest.skip()  直接跳过测试
# unittest.skipIf() 条件为真，跳过测试
# unittest.skipUnless()  条件为假，跳过测试
# unittest.expectedFailure() 预期设置失败
class Test_StartEnd(unittest.TestCase):

    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

class Testadd(Test_StartEnd):
    @unittest.skipIf(4>3,"skip test_add1")
    def test_add(self):
        j = Math(5,5)
        self.assertEqual(j.add_module(),10)
        print("test1")

    @unittest.skip("skip test_add1")
    def test_add1(self):
        j = Math(5, 5)
        self.assertEqual(j.add_module(), 10)
        print("test2")

class TestSub(Test_StartEnd):
    @unittest.skipUnless(1>2,"skip test_add1")
    def test_add(self):
        j = SubMath(15, 5)
        self.assertEqual(j.sub_module(), 10)
        print("test3")

    @unittest.expectedFailure
    def test_add1(self):
        j = SubMath(15, 5)
        self.assertEqual(j.sub_module(), 10)
        print("test4")

class Test(Test_StartEnd):
    @classmethod
    def setUpClass(cls):
        print("Class module start test ......")

    @classmethod
    def tearDownClass(cls):
        print("Class module end ......")
    def test1(self):
        print("test5")

    def test2(self):
        print("test6")

if __name__ == '__main__':
    unittest.main()