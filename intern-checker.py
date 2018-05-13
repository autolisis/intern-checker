#!/usr/bin/env python3

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from os.path import expanduser
from argparse import ArgumentParser

parser = ArgumentParser(
    description='Get current internship application status on Internshala')
parser.add_argument(
    '--login', help='Permit the user to login (Needs to be run once)', action='store_true')
args = parser.parse_args()

# Set the command line options for chromium web driver
chrome_options = webdriver.ChromeOptions()

# Change this to your chrome data dir usually ~/.config/chromium/Default on *nix
path = '~/.config/Chromium'
chrome_options.add_argument(f'user-data-dir={expanduser(path)}')

if not args.login:
    # Makes it headless if there is no need to login
    chrome_options.set_headless()


driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('http://www.internshala.com')
# import pdb
# pdb.set_trace()

if args.login:
    import pdb
    pdb.set_trace()

# Sleep for a while to ensure that the entire page is loaded
sleep(2)
# Get the page source and begin parsing with BS4
soup = BeautifulSoup(driver.page_source, 'lxml')

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
