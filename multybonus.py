from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://partners.int.multibonus.sh/multibonus:aechoh0Kaij4giKai0queigaidoh7h")

sleep(10000)

search_field = driver.find_element(By.NAME, "search")

search_field.send_keys("iphone")
search_field.send_keys(Keys.RETURN)

add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]')
add_to_cart_button.click()

shopping_cart_link = driver.find_element(By.XPATH, '//*[@title="Shopping Cart"]')
shopping_cart_link.click()

assert "product 11" in driver.page_source

sleep(10000)
