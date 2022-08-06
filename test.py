"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


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

assert "product 11" in browser.page_source
browser.quit()

#time.sleep(3)
#browser.quit()


class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, value):
        #self._age == value
        if value <= 18:
            print("Value is less than 18")
        else:
            return self.age == value


p1 = Person('Bob', 'Markson', 22)

print(p1.get_age())
p1.set_age(19)
print(p1.get_age())
"""




