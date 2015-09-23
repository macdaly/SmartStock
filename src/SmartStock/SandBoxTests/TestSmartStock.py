'''
Created on Sep 23, 2015

@author: i056936
'''
import unittest
from SandBox.PyPlotTest import getLocalImportance

class Test(unittest.TestCase):

    def setUp(self):
        self.signal = [1,2,3,6,8,12,10,9,8,10,13,15,17,13,12,11,8,9,10,8,7,8,10,11,9,7,6,5,7,9,13,11,9,8,4,2,4,1]


    def tearDown(self):
        pass

    def testLocalMaxImportance1(self):
        importance = getLocalImportance(5, self.signal, 'max')
        print 'importance found {0}'.format(importance) 
        self.assertEqual(importance, 5, 'wrong importance for local max')
        
    def testLocalMaxImportance2(self):
        importance = getLocalImportance(12, self.signal, 'max')
        self.assertEqual(importance, 25, 'wrong importance for local max')
        
    def testLocalMaxImportance3(self):
        importance = getLocalImportance(18, self.signal, 'max')
        self.assertEqual(importance, 3, 'wrong importance for local max')
        
    def testLocalMaxImportance4(self):
        importance = getLocalImportance(23, self.signal, 'max')
        self.assertEqual(importance, 7, 'wrong importance for local max')
        
    def testLocalMaxImportance5(self):
        importance = getLocalImportance(30, self.signal, 'max')
        print 'importance found {0}'.format(importance)
        self.assertEqual(importance, 17, 'wrong importance for local max')
        
    ########################################
        
    def testLocalMinImportance1(self):
        importance = getLocalImportance(8, self.signal, 'min')
        self.assertEqual(importance, 4, 'wrong importance for local min')
        
    def testLocalMinImportance2(self):
        importance = getLocalImportance(16, self.signal, 'min')
        self.assertEqual(importance, 3, 'wrong importance for local min')
        
    def testLocalMinImportance3(self):
        importance = getLocalImportance(20, self.signal, 'min')
        self.assertEqual(importance, 5, 'wrong importance for local min')
        
    def testLocalMinImportance4(self):
        importance = getLocalImportance(27, self.signal, 'min')
        self.assertEqual(importance, 7, 'wrong importance for local min')
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLocalImportance']
    unittest.main()