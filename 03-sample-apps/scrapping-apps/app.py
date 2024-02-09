from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:\selenium-drivers\chromedriver.exe")

def get_driver():
  # Setting Browser options to enable automation on a linux machine
  options = webdriver.ChromeOptions()
  options.add_argument('disbale-infobars')
  options.add_argument('start-maximized')
  options.add_argument('disable-dev-shm-usage')
  options.add_argument('no-sandbox')
  options.add_argument('disable-blink-features=AutomationControlled')
  options.add_experimental_option('excludeSwitches',['enable-automation'])

  # To get Chrome Driver and set options
  driver = webdriver.Chrome(service= service, options= options)
  # Navigate to a url
  driver.get("https://en.wikipedia.org/wiki/Main_Page")
  return driver

def main():
  # To get driver
  driver = get_driver()
  element = driver.find_element(by="id", value='Welcome_to_Wikipedia')
  return element.text

print('Initiating Test...')
print (main())
print('Test Completed...')