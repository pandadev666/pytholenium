import unittest
import pytholenium as pl
from selenium import webdriver
import os

class TestPytholenium(unittest.TestCase):
    webdriver_path = os.path.dirname(os.path.realpath(__file__)) + r'/test_data/chromedriver'
    webpage_path = os.path.dirname(os.path.realpath(__file__)) + r'/test_data/test.html'

    options = webdriver.ChromeOptions()
    options.binary_location = '/usr/bin/chromium-browser'
    options.add_argument("--no-sandbox")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    options.add_argument("--disable-default-apps")
    driver = webdriver.Chrome(webdriver_path, chrome_options=options)
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




if __name__ == '__main__':
    unittest.main()