import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
load_dotenv()

PATH = '/Users/mack/geckodriver'
driver = webdriver.Firefox(executable_path=PATH)

def get_security_code():
    r = requests.post(os.getenv('SERVER_URL'), data={'body': 'request:security-code'})
    return r

print('Loading page...')
driver.get('https://outlook.com')
print('Loaded!')
signin_btn = driver.find_element(By.LINK_TEXT, 'Sign in')
signin_btn.click()

try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'loginfmt')))

    print('Waiting for email input...')
    email_input = driver.find_element(By.NAME, 'loginfmt')
    email_input.send_keys(os.getenv('EMAIL'), Keys.RETURN)
    print('Done!')

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'passwd')))

    print('Waiting for password input...')
    pwd_input = driver.find_element(By.NAME, 'passwd')
    pwd_input.send_keys(os.getenv('PASSWORD'))
    pwd_input.send_keys(Keys.RETURN)
    print('Done!')

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'iProofPhone')))

    print('2FA initiated...')
    phone_proof = driver.find_element(By.NAME, 'iProofPhone')
    phone_proof.send_keys(os.getenv('DIGITS'), Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'iOttText')))

    proof_text = driver.find_element(By.NAME, 'iOttText')
    time.sleep(5)

    print('Requesting security code...')
    r = requests.post(os.getenv('SERVER_URL'), data={'body': 'request:security-code'})
    print(r.text)
    print('Done!')
except Exception as e:
    print(e)




