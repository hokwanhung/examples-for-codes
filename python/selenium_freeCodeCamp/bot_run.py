# Use JavaScript to help with the identification.
# Open the "Console" tab in Chrome "Inspect", and then type in e.g. 'element = getElementById("")'
# # or 'getElementToClassName()' (sometimes it returns HTMLCollection) to check if the element retrieved is correct.

from selenium.common import WebDriverException
from bot_booking.bot_booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.select_place_to_go(input("Where you want to go: "))
        bot.select_dates(check_in_date=input("What is the check-in date: "),
                         check_out_date=input("What is the check out date: "))  # input format = 'YYYY=MM-DD'
        bot.select_adults(int(input("The number of people: ")))
        bot.click_search()
        bot.apply_filtration()
        bot.refresh()  # A workaround to let our bot grab the data properly.
        bot.report_results()
except WebDriverException as e:
    if 'IN PATH' in str(e):
        print(
            '''
            You are trying to run the bot from command line
            Please add to PATH your Selenium Drivers
            Window:
                set PATH=%PATH%;C:path-to-your-folder
            Linux:
                PATH=$PATH:/path/toyour/folder/
            '''
        )
    else:
        raise
