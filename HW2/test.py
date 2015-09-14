import csv
import unittest
from FFProject import dayData

class dataTestCase(unittest.TestCase):

    def testforDay(self):
        self.assertTrue(dayData('9/9/2015'))

if __name__ == '__main__':
    unittest.main()

    
