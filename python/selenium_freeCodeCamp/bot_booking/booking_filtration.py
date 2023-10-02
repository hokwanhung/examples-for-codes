# This file will include a class with instance methods.
# That will be responsible to interact with our website.
# After we have some results, to appy filtrations.
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        # Asterisk (*) turns variable to arbitrary argument, which allows to pass in multiple argument in one argument.
        star_filtration_box = self.driver.find_element(
            'css selector', f'div[data-filters-group="class"][class="ffa9856b86 ad9a06523f"]')
        star_child_elements = star_filtration_box.find_elements('css selector', '*')

        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    # innerHTML - to find the value inside that HTML tag.
                    star_element.click()

    def sort_price_lowest_first(self):
        menu_element = self.driver.find_element('css selector', 'button[data-testid="sorters-dropdown-trigger"]')
        menu_element.click()
        element = self.driver.find_element(
            'css selector', 'button[data-id="class"][class="fc63351294 ea925ef36a c0c9498572 cddb75f1fd"]')
        element.click()
