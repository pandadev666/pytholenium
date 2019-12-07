import unittest
import pytholenium as pl
from selenium import webdriver
import os
import time

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


    #TC6 - Get element by tag_name
    def test_TC6 (self, driver=driver):
        params = {"tag_name": "sometag"}
        text = pl.get(driver, params).text
        self.assertEqual(text, "Ok?")


    #TC7 - Get element by class_name
    def test_TC7 (self, driver=driver):
        params = {"class_name": "someclass"}
        text = pl.get(driver, params).text
        self.assertEqual(text, "You still reading this?")


    #TC8 - Get element by class_name
    def test_TC8 (self, driver=driver):
        params = {"css_selector": "div#someidforcss"}
        text = pl.get(driver, params).text
        self.assertEqual(text, "Nothing better to do eh?")


    #TC9 - Click button with hardcoded wait time
    def test_TC9 (self, driver=driver):
        params = {"id": "buttonTC9"}
        pl.do(driver=driver, params=params, action="click")
        time.sleep(2) #Element will popup in 1 second, hardcoded double wait time
        text = pl.get(driver=driver, params={"id": "tc9_text"}).text
        self.assertEqual(text, "Thanks!")


    #TC10 - Click button with wait function until div with text is displayed
    def test_TC10 (self, driver=driver):
        params = {"id": "buttonTC10"}
        pl.do(driver=driver, params=params, action="click")
        text_dict = {"xpath": '//*[@id="tc10_text"]/div'}
        obtained_obj = pl.wait(driver=driver, params=text_dict)
        text = obtained_obj.text
        self.assertEqual(text, "Thanks again!")


    #TC11 - Get element by id selector and text attribute
    def test_TC11 (self, driver=driver):
        params = {"id": "someidforcss", "text": "Nothing better to do eh?"}
        text = pl.get(driver=driver, params=params).text
        self.assertEqual(text, "Nothing better to do eh?")


    #TC12 - Get element only by text attribute
    def test_TC12 (self, driver=driver):
        params = {"text": "Nothing better to do eh?"}
        text = pl.get(driver=driver, params=params).text
        self.assertEqual(text, "Nothing better to do eh?")


    #TC13 - Get element only by tag_name_attribute attribute
    def test_TC13 (self, driver=driver):
        params = {"tag_name_attribute": "sometag"}
        text = pl.get(driver=driver, params=params).text
        self.assertEqual(text, "Ok?")


    #TC14 - Get element by name and random tag attribute 
    def test_TC14 (self, driver=driver):
        params = {"name": "program", "random_tag": "anytag"}
        text = pl.get(driver=driver, params=params).text
        self.assertEqual(text, "I'm Pytholenium test.html")


    #TC15 - Get element by name and multiple attributes
    def test_TC15 (self, driver=driver):
        params = {"name": "multiple", "old_city": "barcelona", "new_city": "london"}
        text = pl.get(driver=driver, params=params).text
        self.assertEqual(text, "But don't worry")


    #TC16 - Check an unchecked radio button
    def test_TC16 (self, driver=driver):
        params = {"name": "radio1"}
        selected = pl.get(driver=driver, params=params).is_selected()
        self.assertFalse(selected)
        pl.wait_do(driver=driver, params=params, action="check")
        selected = pl.get(driver=driver, params=params).is_selected()
        self.assertTrue(selected)


    #TC17 - Uncheck a checked radio button
    def test_TC17 (self, driver=driver):
        params = {"name": "radio2"}
        selected = pl.get(driver=driver, params=params).is_selected()
        self.assertTrue(selected)
        pl.wait_do(driver=driver, params=params, action="un_check")
        selected = pl.get(driver=driver, params=params).is_selected()
        self.assertFalse(selected)


    #TC18 - Uncheck an unchecked radio button - Validate error
    def test_TC18 (self, driver=driver):
        params = {"name": "radio1"}
        try:
            pl.wait_do(driver=driver, params=params, action="un_check")
        except Warning as wr:
            self.assertEqual(wr, '#pytholenium-Error005#. When performing action: "check" - Element specified is already checked')


    #TC19 - Check a checked radio button - Validate error
    def test_TC19 (self, driver=driver):
        params = {"name": "radio2"}
        try:
            pl.wait_do(driver=driver, params=params, action="check")
        except Warning as wr:
            self.assertEqual(wr, '#pytholenium-Error005#. When performing action: "check" - Element specified is already unchecked')



if __name__ == '__main__':
    unittest.main()