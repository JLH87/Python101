'''
Created on 16/11/2012

@author: JLH
'''
import unittest
import ex_5

class Test(unittest.TestCase):


    def testdo_plus(self):
    
        self.assertEqual(13, ex_5.do_plus(5, 8), "do_plus() returned a wrong result")
        self.assertEqual(23, ex_5.do_plus(11, 12), "do_plus() returned a wrong result")        
        self.assertEqual(2, ex_5.do_plus(10, 2), "do_plus() returned a wrong result")
        pass



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testdo_plus']
    unittest.main()