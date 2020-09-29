from selenium import webdriver
import os

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)
name = browser.find_element_by_name('firstname')
name.click()
name.send_keys('Valentina')
last_name = browser.find_element_by_name('lastname')
last_name.click()
last_name.send_keys('Lebedeva')
email = browser.find_element_by_name('email')
email.click()
email.send_keys('lebedeva@mail.ru')
file = browser.find_element_by_name('file')

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
file.send_keys(file_path)
btn = browser.find_element_by_css_selector('button')
btn.click()
