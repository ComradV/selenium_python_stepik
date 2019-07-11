from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

ans_element = browser.find_element(By.ID, "answer")
ans_element.send_keys(str(y))

checkbox_element = browser.find_element(By.ID, "robotCheckbox")
checkbox_element.click()

radio_element = browser.find_element(By.ID, "robotsRule")
radio_element.click()


button = browser.find_element_by_css_selector("button.btn")
button.click()

# time.sleep(1)

# находим элемент, содержащий текст
# welcome_text_elt = browser.find_element_by_tag_name("h1")
# # записываем в переменную welcome_text текст из элемента welcome_text_elt
# welcome_text = welcome_text_elt.text

# # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
# assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text