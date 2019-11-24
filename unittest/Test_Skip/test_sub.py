from calculator import *
from StartEnd import *

class Test_add(Setup_tearDown):
    def test_sub(self):
        j = Math(15,5)
        self.assertEqual(j.sub(),10)