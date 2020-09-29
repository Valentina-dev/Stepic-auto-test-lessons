from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'), '$100')
)
book = browser.find_element_by_id('book')
book.click()
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_css_selector('span#input_value.nowrap')
browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
x = x_element.text
y = calc(x)
field = browser.find_element_by_id('answer')
field.click()
field.send_keys(y)
btn = browser.find_element_by_id('solve')
btn.click()
