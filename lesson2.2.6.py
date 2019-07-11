from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return math.log(abs(12*math.sin(int(x)))) 

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

x_elem = browser.find_element(By.ID, "input_value")
x = x_elem.text
y = calc(x)

ans_element = browser.find_element(By.ID, "answer")
ans_element.send_keys(str(y))

checkbox_element = browser.find_element(By.ID, "robotCheckbox")
checkbox_element.click()

radio_element = browser.find_element(By.ID, "robotsRule")
browser.execute_script("return arguments[0].scrollIntoView()", radio_element)
radio_element.click()


button = browser.find_element_by_tag_name("button")
button.click()