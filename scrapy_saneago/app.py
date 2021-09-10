from time import sleep
import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


load_dotenv() 

with webdriver.Chrome() as driver:

    # variables
    saneago_url = 'https://www.saneago.com.br/esi/esi/ESI548SegundaVia.zul'
    account_number = os.getenv('ACCOUNT_NUMBER')
    account_dv = os.getenv('ACCOUNT_DV')

    # Initialize
    wait = WebDriverWait(driver, 5, 3)

    driver.get(saneago_url)

    # Find inputs account and DV
    inputs = driver.find_elements(By.TAG_NAME, 'input')

    # By default, the first and second field is the account
    # and DV respectively
    inputs[0].send_keys(account_number)
    inputs[1].send_keys(account_dv)

    # Click on search button
    driver.find_element(By.CLASS_NAME, 'z-button').click()

    sleep(8)