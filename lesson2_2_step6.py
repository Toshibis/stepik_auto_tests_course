import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)

    robot_checkbox = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    robot_checkbox.click()

    robot_radiobutton = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    robot_radiobutton.click()

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