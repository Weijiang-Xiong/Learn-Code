""" use `python -m unittest --help` to see the manual

    basic usage: 
        python -m unittest test_something.py
        python -m unittest discover -p folder/test*.py

output from `python -m unittest discover -p unittest*.py --verbose`

test_sum (unittest_starter.TestSum) ... ok
test_sum_tuple (unittest_starter.TestSum) ... FAIL

======================================================================
FAIL: test_sum_tuple (unittest_starter.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/default/Learn_Code/python_packages/unittest_starter.py", line 35, in test_sum_tuple
    self.assertEqual(sum((1,2,2)), 6, "should be 6")
AssertionError: 5 != 6 : should be 6

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)


"""


import unittest

class TestSum(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(sum([1,2,3]), 6, "should be 6")

    def test_bad_example(self):
        # this is a test expected to fail, we can catch the error
        with self.assertRaises(TypeError):
            result = sum('oh my god')

if __name__ == "__main__":
    unittest.main()