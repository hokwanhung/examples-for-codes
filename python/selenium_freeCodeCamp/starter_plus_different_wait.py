# Import selenium using `pip install selenium`
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Download and extract the Chrome WebDriver associated to the Chrome Browser version.
# Put it to a location and get the PATH as below.

# Configure in the code level instead of the system level.
# r'' means raw string of something; 'environ' stands for 'environment'.
os.environ['PATH'] += r"C:/Program Files (x86)"
driver = webdriver.Chrome()

# Inspect on the elements we need.
# Load the webpage on the driver.
driver.get("http://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")

# Wait for browser to perform possible changes (setting for all elements).
# But will not wait if the element is already there (different from time.sleep).
driver.implicitly_wait(3)

# Find and click on the element through id.
my_element = driver.find_element('id', 'downloadButton')
my_element.click()

# List of attributes for find_element method:
# https://selenium-python.readthedocs.io/api.html?highlight=#module-selenium.webdriver.common.by
# Explicit wait - more customized and specified waiting for Python in waiting for JavaScript to perform something.
# There is also a fluent wait which creates a repeating cycle with the timeframe to verify/check the condition.
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),  # Element filtration
        'Complete!'  # The expected text
    )
)

# Close the current tab
driver.close()
# Close the whole browser
driver.quit()
