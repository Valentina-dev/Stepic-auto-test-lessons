from selenium import webdriver
import math

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)
btn = browser.find_element_by_css_selector('button')
btn.click()
confirm = browser.switch_to.alert
confirm.accept()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_css_selector('span#input_value.nowrap')
x = x_element.text
y = calc(x)
print(x, y)
field = browser.find_element_by_id('answer')
field.click()
field.send_keys(y)
btn = browser.find_element_by_css_selector('button')
btn.click()
