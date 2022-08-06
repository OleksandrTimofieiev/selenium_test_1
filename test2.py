"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys



class TestSelenium(unittest.TestCase):
    def test_add_to_shopping_cart(self) -> None:
        s = Service('/usr/local/bin/chromedriver')
        browser = webdriver.Chrome(service=s)

        browser.get("http://www.tutorialsninja.com/demo/")

        search_field = browser.find_element(By.NAME, "search")
        search_field.send_keys("iphone")
        search_field.send_keys(Keys.RETURN)

        add_to_cart_button = browser.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]')
        add_to_cart_button.click()

        shopping_cart_link = browser.find_element(By.LINK_TEXT, 'Shopping Cart')
        shopping_cart_link.click()

        self.assertTrue("product 11" in browser.page_source)

        browser.quit()

    def test_delete_from_the_shopping_cart(self):
        self.assertTrue(True)

"""

# Python module to import


print("File two __name__ is set to: {}" .format(__name__))

def function_three():
   print("Function three is executed")

def function_four():
   print("Function four is executed")

if __name__ == "__main__":
   print("File two executed when ran directly")
else:
   print("File two executed when imported")
   #function_three()
