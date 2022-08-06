"""
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

#class TestSeleniumSecond(unittest.TestCase):
    #def software_tab_test(self) -> None:
s = Service('/usr/local/bin/chromedriver')
browser = webdriver.Chrome(service=s)

browser.get("http://www.tutorialsninja.com/demo/")
search_field = browser.find_element(By.XPATH, '//*[@id="menu"]/div[2]/ul/li[5]/a')
search_field.click()
assert "There are no products to list in this categora." in browser.page_source

browser.quit()
"""

# Python module to execute
from test2 import function_three

print("File one __name__ is set to: {}" .format(__name__))

def function_one():
   print("Function one is executed")

def function_two():
   print("Function two is executed")

if __name__ == "__main__":
   print("File one executed when ran directly")
   function_one()
   function_three()
else:
   print("File one executed when imported")
   function_two()


