from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import sys
import requests
from bs4 import BeautifulSoup

import getpass
import time
from pynput.keyboard import Listener, Key

driver = webdriver.Chrome('./chromedriver')

url = str(sys.argv[1])

driver.get(url)


driver.implicitly_wait(10)
player_3 = driver.find_element_by_class_name('table-player-seat-button')
player_3.click()
form = driver.find_element_by_class_name('form-2-input-control input')
form.send_keys(getpass.getuser()[:9])
form.send_keys(Keys.TAB)
form = driver.switch_to.active_element
form.send_keys('1000')
buttom = driver.find_element_by_class_name('button-3.green')
buttom.click()
alert_button = driver.find_element_by_class_name('alert-1-buttons button')
alert_button.click()

time.sleep(10)
current_cards = [0, 1]
values = []
suits = []


def on_press(key):
	if key == Key.space:
		soup = BeautifulSoup(driver.page_source, features="html.parser")
		values = soup.find_all("span", class_="value", limit=2)
		suits = soup.find_all("span", class_="suit sub-suit", limit=2)
		for i in range(2):
			current_cards[i] = values[i].text + suits[i].text
		print(current_cards)


with Listener(on_press=on_press) as listener:
    listener.join()