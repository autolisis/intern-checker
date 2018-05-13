#!/usr/bin/env python3

from selenium import webdriver
import bs4
from time import sleep
from os.path import expanduser

# Set the command line options for chromium web driver
chrome_options = webdriver.ChromeOptions()

# Change this to your chrome data dir usually ~/.config/chromium/ on *nix
path = '~/.config/chromium'
chrome_options.add_argument(f'user-data-dir={expanduser(path)}')

# Sets X-Server WM - Class, can write code to minimize it so it appears headless
chrome_options.add_argument('class=selenium-chrome')

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('http://www.internshala.com')

# Sleep for a while to ensure that the entire page is loaded
sleep(2)

# Get the page source and begin parsing with BS4
soup = bs4.BeautifulSoup(driver.page_source, 'lxml')

# We no longer need the chrome window
driver.close()


# Main parser function that gets the relevant detail from a div tag
def getInternStatus(tag):
    try:
        if tag['class'][0] == 'tooltiptextcontainer':
            return tag.contents[0]
    except:
        return None
    return None


# Pass a list of all the div tags to this function and then filter out all the exceptional cases
internStatuses = list(filter(None, map(getInternStatus, soup.find_all('div'))))


# Print out all the required intern statuses
print(*internStatuses, sep=' | ')
