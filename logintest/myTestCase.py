import unittest
import time
# from time import sleep
from selenium import webdriver


class MyTestCase(unittest.TestCase):

     @classmethod
     def setUpClass(self):
          self.driver = webdriver.Chrome()
          self.driver.maximize_window()
          self.driver.implicitly_wait(30)

     @classmethod
     def tearDownClass(self):
          time.sleep(10) # self.driver.implicitly_wait(30)
          self.driver.quit()



