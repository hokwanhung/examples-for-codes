# To be object-oriented with valid Python bot structure.
import time
import bot_booking.constants as const
from bot_booking.booking_filtration import BookingFiltration
from bot_booking.booking_report import BookingReport
from selenium import webdriver
import os
from prettytable import PrettyTable

# As a constructor, it would be called immediately when an instance is initiated.
class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/Program Files (x86)", teardown=False):
        # It is required to get the driver_path before the program executes in CMD.
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # To ignore CMD irrelevant errors.
        options.add_experimental_option('detach', True)  # To prevent Selenium from auto-closing.
        # super() will receive the name of the inherited class, and then initiate an instance of WebDriver.
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    # __exit__ provide customized tear-down options whenever Python goes out of the indentation.
    # It applies whenever on
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element('css selector', 'button[data-tooltip-text="Choose your currency"]')
        currency_element.click()

        selected_currency_element = self.find_element('css selector',
                                                      f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element('id', 'ss')
        # clear() to clean the existing text.
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element('css selector', 'li[data-i="0"]')
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element('css selector', f'td[data-date="{check_in_date}"')
        check_in_element.click()

        check_out_element = self.find_element('css selector', f'td[data-date="{check_out_date}"')
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element('id', 'xp__guests__toggle')
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element('css selector',
                                                    'button[aria-label="Decrease number of Adults"]')
            decrease_adults_element.click()
            # If the value of adults reaches 1, then we should get out of the while loop.
            adults_value_element = self.find_element('id', 'group_adults')
            adults_value = adults_value_element.get_attribute('value') # Should get back the adult count

            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element('css selector', 'button[aria-label="Increase number of Adults"')

        # Use underscore(_) instead of temporary variable i.
        for _ in range(count - 1):
            increase_button_element.click()

    def click_search(self):
        search_button = self.find_element('css selector', 'button[type="submit"]')
        search_button.click()

    def apply_filtration(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(4, 5)

        filtration.sort_price_lowest_first()

    def report_results(self):
        # time.sleep(10)
        hotel_boxes = self.find_element('class name', 'd4924c9e74')
        report = BookingReport(hotel_boxes)
        table = PrettyTable(
            field_names=['Hotel Name', 'Hotel Price', 'Hotel Score']
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)
