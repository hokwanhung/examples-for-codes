import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# Press Ctrl and 'B' to navigate to that library.
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"C:/Program Files (x86)"
driver = webdriver.Chrome()

driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

driver.implicitly_wait(5)

# Classes with spaces refer to different classes applied to an element.
# Usually the last one would be the most-unique one.
# As the advertisement might not appear at once, use try-except block to prevent predicted error of NoSuchElement.
try:
    no_button = driver.find_element('class name', 'at-cm=no-button')
    no_button.click()
except NoSuchElementException:
    print("No element with this class name. Skipping...")

sum1 = driver.find_element('id', 'sum1')
sum2 = driver.find_element('id', 'sum2')

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(15)

# CSS Selector can perform vague matching (shc as prefixes and suffixes).
# Link: https://www.w3schools.com/cssref/css_selectors.php
btn = driver.find_element('css selector', 'button[onclick="return total()"]')
btn.click()
