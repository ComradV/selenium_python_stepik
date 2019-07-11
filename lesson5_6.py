import math
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver.find_elements(By.CSS_SELECTOR, "button.submit")

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")
elements = browser.find_elements(By.CSS_SELECTOR, ".first_block input")
for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element_by_css_selector("button.btn")
button.click()
