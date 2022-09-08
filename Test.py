#This is Test Code 
#from code import hw
import unittest


class SimpleCalll(unittest.TestCase):

     def setUp(self):
          print "Setup"


     def tearDown(self):
          print "Tear down"


     def test_main(self):
         #Code for the test
         self.assertEqual(3,3,'We are Equal')
         #This will Fail
         self.assertGreater(3,4,"3 is not greater than 4")



if __name__ == '__main__':
    unittest.main()

