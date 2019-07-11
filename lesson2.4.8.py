from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math

def calc(x):
    return math.log(abs(12*math.sin(int(x)))) 

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

button_book = browser.find_element(By.ID, "book")
WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000")
    )
button_book.click()

x_elem = browser.find_element(By.ID, "input_value")
x = x_elem.text
y = calc(x)

ans_element = browser.find_element(By.ID, "answer")
ans_element.send_keys(str(y))

buttonSend = browser.find_element(By.ID, "solve")
buttonSend.click()

button = browser.find_element(By.ID, "button")
button.click()
