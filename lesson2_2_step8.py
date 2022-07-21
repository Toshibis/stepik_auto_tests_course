from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
    input1.send_keys("Toto")
    input2 = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
    input2.send_keys("Otto")
    input3 = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
    input3.send_keys("toto@gmail.com")

    file = browser.find_element(By.XPATH, '//*[@id="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file.send_keys(file_path)

    # file.send_keys('')
    button = browser.find_element(By.XPATH, '/html/body/div/form/button')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()