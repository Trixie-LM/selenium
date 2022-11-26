from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # Эмуляция действий клавиатуры
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains # Отвечает за перетягивание, перелистывание, двойной клик и клик правой кнопкой мыши
import unittest # Библиотека для составления Тест-кейсов
from time import sleep


LOGIN =  '79277956934'
PASSWORD = '!!!!Potrul'

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 30)

   # Открываем сайт
def open_site():
    driver.get("https://multibonus:aechoh0Kaij4giKai0queigaidoh7h@partners.int.multibonus.sh/")
    driver.maximize_window()
    driver.get("https://partners.int.multibonus.sh/")
    driver.find_element(By.XPATH, "//button[ contains(text(), 'ОК') ]").click()


    # Проходим авторизацию пользователя и открываем iframe с лотереей
def authorization():
    driver.find_element(By.XPATH, "//button[ contains(text(), 'Войти') ]").click()
    driver.find_element(By.NAME, "phone-input-desktop").send_keys(LOGIN)
    password_field = driver.find_element(By.NAME, "password-input-desktop")
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.RETURN)
    driver.implicitly_wait(10)
    # driver.find_element(By.XPATH, "//span[ contains(text(), 'Товары и услуги')]")
    wait.until( EC.element_to_be_clickable((By.XPATH, "//span[ contains(text(), 'Товары и услуги')]")))
    driver.get("https://partners.int.multibonus.sh/catalog/onlinecategory/0e80b6dc-0d48-498d-8671-6064343b4ddc?sort=POPULARITY&direction=NEXT")


def accept_agreement():

    first_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//form/span[1]/label')))
    first_checkbox.click()
    second_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//form/span[2]/label')))
    second_checkbox.click()
    accept_button = driver.find_element(By.XPATH, "//span[ contains(text(), 'Принять') ]/..")
    accept_button.click()







if __name__ == '__main__':
    open_site()
    authorization()
    sleep(3)
    driver.switch_to.frame(driver.find_element(By.XPATH, "//html/body/div/main//iframe"))
    accept_agreement()