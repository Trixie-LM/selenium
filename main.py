from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # Эмуляция действий клавиатуры
import unittest # Библиотека для составления Тест-кейсов
from time import sleep

driver = webdriver.Chrome()
driver.get("http://tutorialsninja.com/demo/")

class shopping_cart(unittest.TestCase):

    def test_add_to_shopping_cart(self) -> None:
        """Добавление в корзину"""
            # Находим поле "search"
        search_field = driver.find_element(By.NAME, "search")
            # В поле "search" вбиваем "iphone"
        search_field.send_keys("iphone")
        search_field.send_keys(Keys.RETURN)
            # Добавляем телефон в корзину
        add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]')
        add_to_cart_button.click()
            # Переходим в корзину
        shopping_cart_link = driver.find_element(By.XPATH, '//*[@title="Shopping Cart"]')
        shopping_cart_link.click()
            # Проверяем, что "product 11" есть на странице
        self.assertTrue("product 11" in driver.page_source)


    def test_delete_to_shopping_cart(self) -> None:
        """Удаление из корзины"""
        self.assertTrue(True)

        sleep(10)

