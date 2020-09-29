from selenium import webdriver
import math
import time
link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)
btn = browser.find_element_by_css_selector('button')
btn.click()

new_window = browser.window_handles[1]
turn = browser.switch_to.window(new_window)

time.sleep(1)
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