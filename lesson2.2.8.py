from selenium import webdriver
from selenium.webdriver.common.by import By
# import math
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

name_element = browser.find_element(By.CSS_SELECTOR,"input[name='firstname']")
name_element.send_keys('Ivan')
lastname_element = browser.find_element(By.CSS_SELECTOR,"input[name='lastname']")
lastname_element.send_keys('Ivanov')
email_element = browser.find_element(By.CSS_SELECTOR,"input[name='email']")
email_element.send_keys('Ivan@iv-mail.ru')


file_element = browser.find_element(By.ID, "file")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла 
file_element.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()


import os 
