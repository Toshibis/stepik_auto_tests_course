from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, '//*[@id="num1"]')
    input1_valuex = int(input1.text)

    input2 = browser.find_element(By.XPATH, '//*[@id="num2"]')
    input2_valuex = int(input2.text)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(input1_valuex+input2_valuex))  # ищем элемент с текстом "Python"

    send_button = browser.find_element(By.XPATH, '/html/body/div/form/button')
    send_button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()