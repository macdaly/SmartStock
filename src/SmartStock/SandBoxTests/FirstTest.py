'''
Created on Sep 21, 2015

@author: i056936
'''
import unittest
from SandBox.LearnTest import DummyClass

class Test(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testMultiply(self):
        a = DummyClass(10)
        result = a.multiplyIt(5)
        self.assertEqual(result, 50, "wron result")
        
    def testMultiply2(self):
        a = DummyClass(5)
        result = a.multiplyIt(5)
        self.assertEqual(result, 25, "wron result")
        
    def testIsEven(self):
        even = DummyClass(12)
        odd = DummyClass(13)
        self.assertEqual(even.isEven(), "Even")
        self.assertEqual(odd.isEven(), "Odd")
        
    def testIsEven2(self):
        even = DummyClass(24)
        odd = DummyClass(33)
        self.assertEqual(even.isEven(), "Even")
        self.assertEqual(odd.isEven(), "Odd")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMultiply']
    unittest.main()