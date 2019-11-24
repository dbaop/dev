from calculator import *
from StartEnd import *
import unittest

class Test_add(Setup_tearDown):
    def test_add(self):
        j = Math(5,5)
        self.assertEqual(j.add(),10)

    def test_add(self):
        j = Math(8,5)
        self.assertEqual(j.add(),10)

if __name__ == '__main__':
    unittest.main()
