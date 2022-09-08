#This is Test Code 
from code import hw
import unittest

class test1(unittest):
  def setup(self):
    print("Self up")
  
  def tearDown(self):
    print("Tear down")
  
  def test_main(self):
    # Code for test
    self.assertEqual(3,3,"We are equal")
    
if __name__=="__main__":
  unittest.main()
  

