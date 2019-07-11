from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "num1")
x = x_element.text
y_element = browser.find_element(By.ID, "num2")
y = y_element.text

sum = int(x) + int(y)

select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(str(sum))

button = browser.find_element_by_css_selector("button.btn")
button.click()
