import unittest
import pytholenium as pl
from selenium import webdriver
import os

class TestPytholenium(unittest.TestCase):
    
    webdriver_path = os.path.dirname(os.path.realpath(__file__)) + r'/test_data/chromedriver_v2.42.exe'
    webpage_path = os.path.dirname(os.path.realpath(__file__)) + r'/test_data/test.html'
    driver = webdriver.Chrome(webdriver_path)
    driver.get(webpage_path)

    #TC1 - Get element by id
    def test_TC1 (self, driver=driver):
        #Do the steps
        params = {"id": "hello_there"}
        text = pl.get(driver, params).text
        #Validate
        self.assertEqual(text, "Hey there!")

    #TC2 - Get element by name
    def test_TC2 (self, driver=driver):
        #Do the steps
        params = {"name": "program"}
        text = pl.get(driver, params).text
        #Validate
        self.assertEqual(text, "I'm Pytholenium test.html")




    #TCX - Close driver
    def test_TCX (self, driver=driver):
        #Do the steps
        driver.quit()
        #Validate
        self.assertTrue(True)



if __name__ == '__main__':
    unittest.main()