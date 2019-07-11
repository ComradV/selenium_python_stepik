from selenium import webdriver
from selenium.webdriver.common.by import By
# import math
# import time

# def calc(x):
#     return math.log(abs(12*math.sin(int(x)))) 

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/cats.html"
browser.get(link)

# time.sleep(1)
# button = browser.find_element(By.CSS_SELECTOR, "button.btn")
# button.click()

# time.sleep(1)

# new_window = browser.window_handles[1]
# browser.switch_to.window(new_window)

# x_elem = browser.find_element(By.ID, "input_value")
# x = x_elem.text
# y = calc(x)

# ans_element = browser.find_element(By.ID, "answer")
# ans_element.send_keys(str(y))

button = browser.find_element(By.ID, "button")
button.click()
