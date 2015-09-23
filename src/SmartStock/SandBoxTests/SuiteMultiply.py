'''
Created on Sep 21, 2015

@author: i056936
'''
import unittest
from FirstTest import Test


class SuiteMultiply(unittest.TestSuite):


    def setUp(self):
        self.addTest(Test('testMultiply'))
        self.addTest(Test('testMultiply2'))


    def tearDown(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    result = unittest.TestResult()
    suite = SuiteMultiply()
    suite.run(result)
    print "number of tests {tests}".format(tests = suite.countTestCases())  
    unittest.main(module='SuiteMultiply')