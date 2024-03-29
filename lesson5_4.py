import math
from selenium import webdriver

# from selenium.webdriver.common.by import By
# driver.find_elements(By.CSS_SELECTOR, "button.submit")

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)

link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
link.click()

input1 = browser.find_element_by_name("first_name")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_css_selector("form div:nth-child(3) input")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_css_selector("form div:nth-child(4) input")
input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()