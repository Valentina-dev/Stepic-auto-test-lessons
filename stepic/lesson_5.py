import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


treasure = browser.find_element_by_id('treasure')
number = treasure.get_attribute('valuex')
print(number)

y = calc(number)
field = browser.find_element_by_id('answer')
field.click()
field.send_keys(y)
robot = browser.find_element_by_css_selector('[id="robotCheckbox"]')
robot.click()
radio_batton = browser.find_element_by_css_selector('[value="robots"]')
radio_batton.click()
button = browser.find_element_by_css_selector('button')
button.click()

