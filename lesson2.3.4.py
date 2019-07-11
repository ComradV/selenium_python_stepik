from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return math.log(abs(12*math.sin(int(x)))) 

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

alert = browser.switch_to_alert()
alert.accept()

x_elem = browser.find_element(By.ID, "input_value")
x = x_elem.text
y = calc(x)

ans_element = browser.find_element(By.ID, "answer")
ans_element.send_keys(str(y))

button = browser.find_element_by_tag_name("button")
button.click()
