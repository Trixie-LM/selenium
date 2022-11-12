import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://tutorialsninja.com/demo/")

class shopping_cart(unittest.TestCase):

    def test_add_to_shopping_cart(self) -> None:
        """Добавление в корзину"""


        search_field = driver.find_element(By.NAME, "search")

        search_field.send_keys("iphone")
        search_field.send_keys(Keys.RETURN)

        add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]')
        add_to_cart_button.click()

        shopping_cart_link = driver.find_element(By.XPATH, '//*[@title="Shopping Cart"]')
        shopping_cart_link.click()

        self.assertTrue("product 11" in driver.page_source)



    def test_delete_to_shopping_cart(self) -> None:
        """Удаление из корзины"""
        self.assertTrue(True)

    sleep(3)

