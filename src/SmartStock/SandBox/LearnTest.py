'''
Created on Sep 21, 2015

@author: i056936
'''

class DummyClass(object):
    '''
    classdocs
    '''


    def __init__(self, theNumber):
        '''
        Constructor
        '''
        self.itsNumber = theNumber    
    
    def multiplyIt(self, multplier):
        return self.itsNumber * multplier
    
    def isEven(self):
        if self.itsNumber % 2 == 0:
            return "Even"
        return "Odd"