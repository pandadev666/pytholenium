import unittest
import pytholenium as pl
from selenium import webdriver
import os

class TestPytholenium(unittest.TestCase):
    #Chromedriver and webpage paths in Travis-CI
    webdriver_path = os.path.dirname(os.path.realpath(__file__)) + r'/test_data/chromedriver'
    webpage_path = "file://" + os.path.dirname(os.path.realpath(__file__)) + r'/test_data/test.html'

    #Set up the webdriver in headless mode for Travis-CI
    options = webdriver.ChromeOptions()
    options.binary_location = '/usr/bin/google-chrome'
    options.add_argument("--no-sandbox")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    options.add_argument("--disable-default-apps")
    driver = webdriver.Chrome(webdriver_path, chrome_options=options)
    #Open the webpage
    driver.get(webpage_path)


    #TC1 - Get element by id
    def test_TC1 (self, driver=driver):
        params = {"id": "hello_there"}
        text = pl.get(driver, params).text
        self.assertEqual(text, "Hey there!")


    #TC2 - Get element by name
    def test_TC2 (self, driver=driver):
        params = {"name": "program"}
        text = pl.get(driver, params).text
        self.assertEqual(text, "I'm Pytholenium test.html")


    #TC3 - Get element by xpath
    def test_TC3 (self, driver=driver):
        params = {"xpath": "/html/body/div[3]"}
        text = pl.get(driver, params).text
        self.assertEqual(text, "I'm only created for the unit tests")


    #TC4 - Get element by link_text
    def test_TC4 (self, driver=driver):
        params = {"link_text": "To validate everything is working"}
        text = pl.get(driver, params).text
        self.assertEqual(text, "To validate everything is working")

    #TC5 - Get element by partial link_text
    def test_TC5 (self, driver=driver):
        params = {"partial_link_text": "You can just"}
        text = pl.get(driver, params).text
        self.assertEqual(text, "You can just ignore this")


if __name__ == '__main__':
    unittest.main()