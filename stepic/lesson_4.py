import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_css_selector('span#input_value.nowrap')
x = x_element.text
y = calc(x)
print(x, y)
field = browser.find_element_by_id('answer')
field.click()
field.send_keys(y)
robot = browser.find_element_by_css_selector('[id="robotCheckbox"]')
robot.click()
radio_batton = browser.find_element_by_css_selector('[value="robots"]')
radio_batton.click()
button = browser.find_element_by_css_selector('button')
button.click()
