# This file is going to include method that will parse the specific data that we need from each one of the deal boxes.
from selenium.webdriver.remote.webelement import WebElement


class BookingReport: # Do not need to inherit anything.
    def __init__(self, boxes_selection_element: WebElement):
        self.boxes_selection_element = boxes_selection_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_selection_element.find_elements(
            'css selector',
            f'div[data-testid="property-card"][class="a826ba81c4 fe821aea6c fa2f36ad22 afd256fc79 d08f526e0d ed11e24d01 ef9845d4b3 da89aeb942"]'
        )

    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            # Pulling the hotel name
            hotel_name = deal_box.find_element(
                'css selector',
                f'div[data-testid="title"][class="fcab3ed991 a23c043802"]').get_attribute('innerHTML').strip()
            # Pulling the hotel price
            hotel_price = deal_box.find_element(
                'css selector',
                f'span[data-testid="price-and-discounted-price"]').get_attribute('innerHTML').strip()
            hotel_score = deal_box.find_element(
                'css selector',
                f'div[class="b5cd09854e d10a6220b4"]'
            ).get_attribute('innerHTML').strip()

            collection.append([hotel_name, hotel_price, hotel_score])
        return collection
