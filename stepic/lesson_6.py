from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id('num1')
    num2 = browser.find_element_by_id('num2')
    sum = int(num1.text) + int(num2.text)
    print(sum)
    x = str(sum)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(x)
    btn = browser.find_element_by_css_selector('button').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
