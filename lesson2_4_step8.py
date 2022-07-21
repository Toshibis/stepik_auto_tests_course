from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), "$100"))
    button = browser.find_element(By.XPATH, '//*[@id="book"]')
    button.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)

    button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()